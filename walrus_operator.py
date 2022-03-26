# walrus operator :=

# assignment expression aka walrus operator
# assigns values to variables as part of a larger expression

# print(happy = true)  # Will get Error

print(happy := True)

foods = list()
while food := input("What food do you like?: ") != "quit":
    foods.append(food)

