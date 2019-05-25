import unittest
import json
import requests
import datetime
import pytz
import random
from timestampapp import timestamp

class TimeStampTestCase(unittest.TestCase):
	def setUp(self):
		timestamp.app.testing = True
		self.app = timestamp.app.test_client()

	def test_default_timestamp_retrieval(self):
		resp = self.app.get('/timestamp')
		curr_timestamp = '{0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.utcnow())
		self.assertEqual(json.loads(resp.data.decode("utf-8"))['currentTime'], curr_timestamp) 

	def test_timezone_timestamp_retrieval(self):
		tz = random.choice(pytz.all_timezones)
		resp = self.app.get('/timestamp?tz='+tz)
		timezone = pytz.timezone(tz)
		local_time = pytz.utc.localize(datetime.datetime.utcnow(), is_dst=None).astimezone(timezone)
		formatted_time = '{0:%Y-%m-%d %H:%M:%S}'.format(local_time)
		self.assertEqual(json.loads(resp.data.decode("utf-8"))['currentTime'], formatted_time)

	def test_error_response(self):
		resp = self.app.get('/timestamp?tz=fakezone')
		self.assertEqual(json.loads(resp.data.decode("utf-8"))['error'],"Unknown Timezone Given: 'fakezone'")

if __name__ == '__main__':
	unittest.main()
