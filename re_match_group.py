import re


pattern = r"egg(spam)*"

if re.match(pattern, "egg"):
    print("Match * 1")

if re.match(pattern, "eggspamspamspamegg"):
    print("Match * 2")

if re.match(pattern, "spam"):
    print("Match * 3")

pattern = r"egg(spam)"
# pattern = r"eggspam"

if re.match(pattern, "egg"):
    print("Match group 1")

if re.match(pattern, "eggspamspamspamegg"):
    print("Match group 2")

if re.match(pattern, "spam"):
    print("Match group 3")
