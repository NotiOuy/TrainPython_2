# set = collection which is unordered, unindexed. No duplicate values

utensils = {"fork", "spoon", "knife", "spoon", "spoon", "spoon"}
dishes = {"bowl", "plate", "cup", "spoon"}

#utensils.add("napkin")
#utensils.remove("knife")
#utensils.clear()
#utensils.update(dishes)
#dinner_table = utensils.union(dishes)

for x in utensils:
    print(x, end=" ")

print()
#print(utensils.difference(dishes))
print(utensils.intersection(dishes))