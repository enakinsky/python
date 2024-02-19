import re

def find_dates(string):
    pattern = r"\d{1,2}\s\w+\s\d{4}"
    dates = re.findall(pattern, string)
    return dates
