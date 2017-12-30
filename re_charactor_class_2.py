import re


pattern = r"[A-Z][A-Z][0-9]"
# pattern的前两位必须是大写字母，第三位必须是数字

if re.search(pattern, "LS8"):
    print("Match 1")

if re.search(pattern, "E3"):
    print("Match 2")

if re.search(pattern, "1ab"):
    print("Match 3")
