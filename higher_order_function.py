# Higher Order Function = a function that either:
#                           1. accept a function as an argument
#                               or
#                           2. returns a function
#                           (In python, function are also treated as object)

def loud(text):
    return text.upper()


def quite(text):
    return text.lower()


def hello(func):
    text = func("Hello")
    print(text)


hello(quite)
hello(loud)


def divisor(x):
    def dividend(y):
        return y / x
    return dividend


divide = divisor(353)
print((divide(1000)))
