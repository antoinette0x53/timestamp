#!/bin/python3

# importing flask to run application server
from flask import Flask
from flask import request
import json 
import datetime
import pytz
import urllib.parse

app = Flask(__name__)
# Setting method so that app only accepts GET requests
@app.route('/',methods=['GET'])
def get():
	# if timezone is supplied then return time in for that timezone, otherwise return UTC time.
	tz = request.args.get('tz')
	utc_time = datetime.datetime.utcnow()
	if tz is not None and tz is not '':
		try:
			timezone = pytz.timezone(urllib.parse.unquote(tz))
			local_time = pytz.utc.localize(utc_time, is_dst=None).astimezone(timezone)
			formatted_time = '{0:%Y-%m-%d %H:%M:%S}'.format(local_time)
		except pytz.exceptions.UnknownTimeZoneError as e:
			return json.dumps({"currentTime":"","error":"Unknown Timezone Given: "+str(e)})
	else:	
		formatted_time = '{0:%Y-%m-%d %H:%M:%S}'.format(utc_time)	
	return json.dumps({"currentTime":str(formatted_time)})

if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5000)
