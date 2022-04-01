# scope = region that a variable is recognized
#         A variable is only available from inside the region it is created.
#         A global and locally scoped versions of a variable can be created

name = "Name in global scope."  # Global scope (available inside & outside functions)


def out_name():
    name_function = "Name of function. In local scope."  # Local scope (available only inside this function
    print(name_function)


out_name()
print(name)
