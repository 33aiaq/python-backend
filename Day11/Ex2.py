import re

def validate_email(email):
    pattern = r'^[\w.-]+@[A-Za-z0-9-]+\.[A-Za-z]{2,4}$'
    return bool(re.match(pattern, email))

emails = [
    "ahmad@example.com",
    "saif123@my-site.net",
    "mohammed@server.org",
    "invalid.email.com",
    "user@site.c",
    "user@site.comm"
]

for email in emails:
    if validate_email(email):
        print(f"{email} is a valid email.")
    else:
        print(f"{email} is NOT a valid email.")
