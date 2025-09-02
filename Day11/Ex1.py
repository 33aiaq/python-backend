import re
from datetime import datetime
import pytz

def validate_email(email):
    pattern = r'^[\w.-]+@[A-Za-z0-9-]+\.[A-Za-z]{2,4}$'
    return bool(re.match(pattern, email))

emails = [
    "ahmad@example.com",
    "saif@example.net",
    "mohammed@example",
    "invalid.email.com"
]

for email in emails:
    if validate_email(email):
        print(f"{email} is a valid email.")
    else:
        print(f"{email} is NOT a valid email.")

timezones = ["UTC", "Asia/Amman", "Europe/London", "America/New_York"]

utc = pytz.utc
now_utc = datetime.now(utc)

for tz_name in timezones:
    tz = pytz.timezone(tz_name)
    tz_time = now_utc.astimezone(tz)
    print(f"{tz_name}: {tz_time.strftime('%Y-%m-%d %H:%M:%S')}")
