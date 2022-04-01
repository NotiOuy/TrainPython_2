#
# if __name__ = '__main__'
#
# 1. Module can be run as a standalone program
# 2. Module can be imported and used by other modules

# Python interpreter sets "special variable", one of which is __name__
# then Python will execute the code found within __main__
# the initial module being main
def hello():
    print("Hello!")


if __name__ == '__main__':
    print("Run __main__")
#    hello()


