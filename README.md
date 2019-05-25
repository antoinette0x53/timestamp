# Timestamp

## Timestamp web service
_A simple web service that returns a json formatted timestamp_

`GET /timestamp` will return the current UTC json formatted timestamp

`GET /timestamp?tz={timezone}` will return the a json formatted timestamp in a valid timezone from the pytz.all_timezone list.

Example output: `{"currentTime": "2019-05-25 03:06:19"}`

## Timestamp Client
_A simple client to connect to the timestamp web service and parse and display the date and time_

$ python3 get_timestamp.py {timezone} will return the date and time in a human readable format.

Example:
```
$ python3 get_timestamp.py America/Chicago
Requesting current time for timezone: America/Chicago
Today is May 24, 2019 and the current time is 10:46:30 PM.

```
