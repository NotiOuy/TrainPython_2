# zip(*iterables) = aggregate elements from two or more iterables )list, tuples, sets, etc.)
#                   creates a zip object with paired elements stored in tuples for each element

usernames = ["Dude", "Bro", "Mister"]
passwords = ("password", "abcds2453", "questingtua")
login_date = ["35/45/23424", "1/32/2244", "32/35/2343"]

users = zip(usernames, passwords, login_date)

for i in users:
    print(i)
