import re


pattern = r"(.+) \1"
"""Note, that "(.+) \1" is not the same as "(.+) (.+)", because \1 refers to
the first group's subexpression, which is the matched expression itself, and
not the regex pattern."""

match = re.match(pattern, "word word")
if match:
    print("Match 1")
    print(match.group(1))
    print(match.group())

match = re.match(pattern, "?! ?!")
if match:
    print("Match 2")
    print(match.group(1))
    print(match.group())

match = re.match(pattern, "abc cde")
if match:
    print("Match 3")
    print(match.group(1))
    print(match.group())

pattern = r"(.+) (.+) (.+) \1"

match = re.match(pattern, "abc bca cab abc")  # \1 represent abc
if match:
    print("Match 1-1")

match = re.match(pattern, "abc bca cab bca")
if match:
    print("Match 1-2")

match = re.match(pattern, "abc bca cab cab")
if match:
    print("Match 1-3")

pattern = r"(.+) (.+) (.+) \2"

match = re.match(pattern, "abc bca cab abc")
if match:
    print("Match 2-1")

match = re.match(pattern, "abc bca cab bca")  # \2 represent bca
if match:
    print("Match 2-2")

match = re.match(pattern, "abc bca cab cab")
if match:
    print("Match 2-3")

pattern = r"(.+) (.+) (.+) \3"

match = re.match(pattern, "abc bca cab abc")
if match:
    print("Match 3-1")

match = re.match(pattern, "abc bca cab bca")
if match:
    print("Match 3-2")

match = re.match(pattern, "abc bca cab cab")  # \3 represent cab
if match:
    print("Match 3-3")
