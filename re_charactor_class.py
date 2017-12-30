import re


pattern = r"[aeiou]"

if re.search(pattern, "grey"):
    print("Match 1")

if re.search(pattern, "qwertyuiop"):
    print("Match 2")

if re.search(pattern, "rhythm myths"):
    print("Match 3")
# The pattern [aeiou] in the search function matches all strings that contain
# any one of the characters defined.

pattern = r"[abc][def]"
if re.search(pattern, "bb"):
    print("Match abc")

if re.search(pattern, "ee"):
    print("Match ee")

if re.search(pattern, "abc"):
    print("Match abc")

if re.search(pattern, "bd"):
    print("Match 3")

if re.search(pattern, "af"):
    print("Match 4")
