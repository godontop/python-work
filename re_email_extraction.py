import re


pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+)"
str = "Please contact info@sololearn.com for assistance"

match = re.search(pattern, str)
if match:
    print(match.group())
# In case the string contains multiple email addresses, we could use the
# re.findall method instead of re.search, to extract all email addresses.
