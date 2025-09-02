import re
from datetime import datetime
import pytz

logs = [
    "[2025-08-21 14:30:00 UTC] User: Anas Action: Login",
    "[2025-08-21 15:00:00 UTC] User: Yousef Action: Logout",
    "[2025-08-21 16:15:00 UTC] User: Hamza Action: Upload"
]

pattern = r"\[(.*?) UTC\] User: (\w+) Action: (\w+)"

utc = pytz.utc
amman = pytz.timezone("Asia/Amman")

for log in logs:
    match = re.search(pattern, log)
    if match:
        timestamp_str, user, action = match.groups()
        
        dt_utc = datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M:%S")
        dt_utc = utc.localize(dt_utc)
        
        dt_amman = dt_utc.astimezone(amman)
        
        print(f"User: {user} | Action: {action} | Time (Amman): {dt_amman.strftime('%Y-%m-%d %H:%M:%S')}")
