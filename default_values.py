def function(x, y, food="spam"):
    print(food)

function(1, 2)
# The argument '1' is passed in to parameter x, the argument '2' is passed in
# to y, no argument is passed in to the parameter food (so the default is
# used).
function(3, 4, "egg")
# "egg" passed in to parameter food

"""
In case the argument is passed in, the default value is ignored.
If the argument is not passed in, the default value is used.
"""

# passed in means
# It means if you do not assign something to "food", then it will default to
# what was already "passed in"("spam").
