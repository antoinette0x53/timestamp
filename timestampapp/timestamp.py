#!/bin/python3

# importing flask to run application server
from flask import Flask
from flask import request
from flask.logging import default_handler
import logging
import json 
import datetime
import pytz
import urllib.parse

# Ref: http://flask.pocoo.org/docs/1.0/logging/ - Injecting Request Information
class RequestFormatter(logging.Formatter):
	def format(self, record):
		record.url = request.url
		record.remote_addr = request.remote_addr
		return super().format(record)

app = Flask(__name__)
# Setting method so that app only accepts GET requests
@app.route('/timestamp',methods=['GET'])
def get():
	app.logger.info("New timestamp request.")
	# if timezone is supplied then return time in for that timezone, otherwise return UTC time.
	tz = request.args.get('tz')
	utc_time = datetime.datetime.utcnow()
	if tz is not None and tz is not '':
		try:
			timezone = pytz.timezone(urllib.parse.unquote(tz))
			local_time = pytz.utc.localize(utc_time, is_dst=None).astimezone(timezone)
			formatted_time = '{0:%Y-%m-%d %H:%M:%S}'.format(local_time)
		except pytz.exceptions.UnknownTimeZoneError as e:
			app.logger.error("Unknown Time Zone Received.")
			return json.dumps({"currentTime":"","error":"Unknown Timezone Given: "+str(e)})
	else:	
		formatted_time = '{0:%Y-%m-%d %H:%M:%S}'.format(utc_time)
	app.logger.info("Sending timestamp.")	
	return json.dumps({"currentTime":str(formatted_time)})

if __name__ == '__main__':
	formatter = RequestFormatter(
        '%(asctime)s - [%(levelname)s] - %(remote_addr)s requested %(url)s: %(message)s'
	)
	default_handler.setFormatter(formatter)
	fh = logging.FileHandler('timestamp.log')
	fh.setLevel(logging.DEBUG)
	fh.setFormatter(formatter)
	app.logger.addHandler(fh)
	app.logger.setLevel(logging.DEBUG)
	app.run(host='0.0.0.0',port=5000)
