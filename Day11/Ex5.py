from datetime import datetime
import pytz

def convert_timezone(time_str, from_tz, to_tz):
    from_timezone = pytz.timezone(from_tz)
    to_timezone = pytz.timezone(to_tz)
    naive_dt = datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
    from_dt = from_timezone.localize(naive_dt)
    to_dt = from_dt.astimezone(to_timezone)
    return to_dt.strftime("%Y-%m-%d %H:%M:%S")

time_str = "2023-11-05 14:30:00"
converted_time = convert_timezone(time_str, "US/Eastern", "UTC")
print("Converted time:", converted_time)
