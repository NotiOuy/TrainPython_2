drinks = ["Coffee", "Soda", "Tea"]
dinner = ["Pizza", "Hamburger", "hotdog"]
dessert = ["Cake", "ice cream"]

food = [drinks, dinner, dessert]

for i in food:
    for j in i:
        print(j, end=" ")
    print()