# str.format() = optional method that gives users
#                more control when displaying output

animal = "cow"
item = "moon"

print("The " + animal + " jumped over the " + item)
print("The {} jumped over the {}".format(animal, item))
print("The {1} jumped over the {0}".format(item, animal))  # positional argument
print("The {animal} jumped over the {item}".format(animal="cat", item="tree"))  # keyword argument

random_text = "The {} jumped over the {}"
print(random_text.format("dog", "house"))

print("=========================================================")
number = 222222
print("The number from 222222 is {:,}".format(number))
print("The number from 222222 is {:b}".format(number))
print("The number from 222222 is {:o}".format(number))
print("The number from 222222 is {:X}".format(number))
print("The number from 222222 is {:E}".format(number))
