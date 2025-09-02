import re
from datetime import datetime, timezone, timedelta

def parse_log_timestamps(log):
    pattern = r'\[(\d{2}/[A-Za-z]{3}/\d{4}:\d{2}:\d{2}:\d{2}) \+\d{4}\]'
    matches = re.findall(pattern, log)
    result = []
    for ts in matches:
        dt = datetime.strptime(ts, "%d/%b/%Y:%H:%M:%S")
        dt_utc = dt.replace(tzinfo=timezone.utc)
        result.append(dt_utc.strftime("%Y-%m-%d %H:%M:%S"))
    return result

log_text = '''
127.0.0.1 - - [21/Aug/2025:14:30:00 +0000] "GET /index.html HTTP/1.1"
127.0.0.1 - - [21/Aug/2025:15:45:12 +0000] "POST /form HTTP/1.1"
'''

timestamps = parse_log_timestamps(log_text)
print("Extracted timestamps in UTC:")
for t in timestamps:
    print(t)
