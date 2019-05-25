#!/bin/python3

import requests
import json
import datetime
import urllib.parse

# Settings for connection to timestamp service
timezone = 'America/Chicago'
host = 'http://0.0.0.0'
port = '5000'

try:
	if timezone is not '':
		print('Requesting current time for timezone: '+timezone)
		timezone = urllib.parse.quote(timezone, safe='')
	else:
		print('Requesting current time in UTC time.')
	r = requests.get(host+':'+port+'/timestamp?tz='+timezone)
	if r.status_code == 200:
		try:
			timestamp = datetime.datetime.strptime(r.json()['currentTime'],'%Y-%m-%d %H:%M:%S')
			timeString = 'Today is {0:%B} {0:%d}, {0:%Y} and the current time is {0:%I:%M:%S %p}.'.format(timestamp)
			print(timeString)
		except ValueError as e:
			print(r.json()['error'])
	else:
		print("Non 200 status returned from server.")
except requests.exceptions.RequestException as e:
	print("Connection Error. Make sure the timestamp service is running.")


