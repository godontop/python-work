import re


pattern = r"gr.y"
# .(dot) matches any charactor(just one charactor)

if re.match(pattern, "grey"):
    print("Match 1")

if re.match(pattern, "gray"):
    print("Match 2")

if re.match(pattern, "gr$y"):
    print("Match 3")

if re.match(pattern, "blue"):
    print("Match 4")

pattern = r"^gr.y$"

if re.match(pattern, "grey"):
    print("Match 5")

if re.match(pattern, "gray"):
    print("Match 6")

if re.match(pattern, "stingray"):
    print("Match 7")
