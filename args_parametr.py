# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments
def sum_two_numbers(num1, num2):
    return num1 + num2


print(sum_two_numbers(4, 32))


def sum_many_numbers(*numbers):
    sum_varying_amount_arguments = 0
    for i in numbers:
        sum_varying_amount_arguments += i
    return sum_varying_amount_arguments


print(sum_many_numbers(34, 45, 32, 65, 49, 9))


# **kwargs = parameter that will pack all arguments into a dictionary
#            useful so that a function can accept a varying amount of keyword arguments
def hello(**kwargs):
    print("Hello", end=" ")
    for key, value in kwargs.items():
        print(value, end=" ")


hello(first="Man", last="Code")
