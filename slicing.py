# slicing = create a substring by extracting elements from another string
#               indexing[] or slice()
#               [start:stop:step]

name = "Turtle Bruh"
first_name = name[0:6]
last_name = name[7:]
funky_name = name[0::2]
reverse_name = name[::-1]
print(f"First name: {first_name} / Last name: {last_name}")
print(f"Funky name: {funky_name} / Revers name {reverse_name}")

website = "http://google.com"
slice_website = slice(7, -4)
slice_name = slice(3, 6)

print(f"Slice of the site: {website[slice_website]}, Slice of the name: {name[slice_name]}")
