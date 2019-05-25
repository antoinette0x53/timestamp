# Timestamp

## Timestamp web service
_A simple web service that returns a json formatted timestamp_

`GET /timestamp` will return the current UTC json formatted timestamp

`GET /timestamp?tz={timezone}` will return the a json formatted timestamp in a valid timezone from the pytz.all_timezone list.

Example output: `{"currentTime": "2019-05-25 03:06:19"}`

**Running the web service**
Update `timestamp.py` to use the ip address and port of your choosing and run `$ python3 timestamp.py`

## Timestamp Client
_A simple client to connect to the timestamp web service and parse and display the date and time_

**Note: Update get_timestamp.py to use correct ip address and port if changed in timestamp.py**

`$ python3 get_timestamp.py {timezone}` will return the date and time in a human readable format.

Example:
```
$ python3 get_timestamp.py America/Chicago
Requesting current time for timezone: America/Chicago
Today is May 24, 2019 and the current time is 10:46:30 PM.

```
## Considerations
The data being sent (the current time) isn't considered personal or privileged and as such did not warrant the same level of data integrity and privacy security considerations that might need to be made for more sensitive information. Had this not been the case, TLS encryption and authentication would be implemented.
