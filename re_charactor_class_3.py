import re


pattern = r"[^A-Z]"
# pattern match any charactor other than [A-Z]

if re.search(pattern, "this is all quiet"):
    print("Match 1")

if re.search(pattern, "AbCdEfG123"):
    print("Match 2")
    # Output: Match 2
    # pattern 匹配除了[A-Z]的任意字符

if re.search(pattern, "THISISALLSHOUTING"):
    print("Match 3")
