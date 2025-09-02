import re

def extract_dates(text):
    pattern = r'\b\d{1,2}[-/]\d{1,2}[-/]\d{4}\b'
    return re.findall(pattern, text)

text = "noor was born on 21-08-1995, hassan on 05/11/2000, and wessam on 03-7-1988."

dates = extract_dates(text)
print("Dates found:", dates)
