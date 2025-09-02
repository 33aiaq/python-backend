from datetime import datetime, timedelta

birthdate_str = input("Enter your birthdate (YYYY-MM-DD): ")
birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d")

now = datetime.now()

this_year_birthday = birthdate.replace(year=now.year)
if this_year_birthday < now:
    next_birthday = birthdate.replace(year=now.year + 1)
else:
    next_birthday = this_year_birthday

time_remaining = next_birthday - now

days = time_remaining.days
hours, remainder = divmod(time_remaining.seconds, 3600)
minutes, _ = divmod(remainder, 60)

print(f"Time until your next birthday: {days} days, {hours} hours, {minutes} minutes")
