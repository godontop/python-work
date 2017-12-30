import re


pattern = r"\b(cat)\b"
# "\b(cat)\b" 匹配"cat"或者任何包含cat且字符c前为\W字符、字符t后也为\W字符的字符串
# "\b(cat)\b" basically matches the word "cat" surrounded by word boundaries.

match = re.search(pattern, "The cat sat!")
if match:
    print("Match 1")

match = re.search(pattern, "We s>cat<tered?")
if match:
    print("Match 2")

match = re.search(pattern, "The-cat-sat!")
if match:
    print("Match 3")

match = re.search(pattern, "The.cat.sat!")
if match:
    print("Match 4")

match = re.search(pattern, "The+cat*sat!")
if match:
    print("Match 5")

match = re.search(pattern, "The_cat_sat!")
if match:
    print("Match 9")

match = re.search(pattern, "We scatterd.")
if match:
    print("Match 10")
