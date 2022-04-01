# lambda function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression.
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time, throw-away)
#
#   lambda parameters:expression


double = lambda x: x * 2
print(double(4))
multiply = lambda x, y: x * y
print(multiply(234, 5))
add = lambda x, y, z: x + y + z
print(add(24, 54, 382))
