import re


pattern = r"egg(spam)*"
# (spam) represents a group in the pattern

if re.match(pattern, "egg"):
    print("Match * 1")

if re.match(pattern, "eggspamspamegg"):
    print("Match * 2")

if re.match(pattern, "spam"):
    print("Match * 3")

pattern = r"g+"

if re.match(pattern, "g"):
    print("Match + 1")

if re.match(pattern, "gggggggggggggg"):
    print("Match + 2")

if re.match(pattern, "abc"):
    print("Match + 3")

pattern = r"ice(-)?cream"

if re.match(pattern, "ice-cream"):
    print("Match ? 1")

if re.match(pattern, "icecream"):
    print("Match ? 2")

if re.match(pattern, "sausages"):
    print("Match ? 3")

if re.match(pattern, "ice--ice"):
    print("Match ? 4")

pattern = r"9{1,3}$"
# end with 9 or 99 or 999
# re.match(pattern, "string") just match 9 or 99 or 999

if re.match(pattern, "9"):
    print("Match {} 1")

if re.match(pattern, "999"):
    print("Match {} 2")

if re.match(pattern, "9999"):
    print("Match {} 3")

pattern = r"gr(a|e)y"

match = re.match(pattern, "gray")
if match:
    print("Match | 1")

match = re.match(pattern, "grey")
if match:
    print("Match | 2")

match = re.match(pattern, "griy")
if match:
    print("Match | 3")
