def function(
        var1, var2, var3,
        var4):
    return 1


foo = function(
    1, 3,
    4, 5)

print(foo)
# No extra indentation.
if (this_is_one_thing and
        that_is_another_thing):
    do_something()

# Add a comment, which will provide some distinction in editors
# supporting syntax highlighting.
if (this_is_one_thing and
        that_is_another_thing):
    # Since both conditions are true, we can frobnicate.
    do_something()

# Add some extra indentation on the conditional continuation line.
if (this_is_one_thing
        and that_is_another_thing):
    do_something()

my_list = [
    1, 2, 3,
    4, 5, 6
]

result = function(
    1, 3,
    3, 4
)
