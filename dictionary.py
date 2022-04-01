# dictionary = A changeable, unordered collection of unique key:value pairs
# Fast because they use hashing, allow us to access a value quickly

capitals = {"USA": "Washington DC",
            "India": "New Dehli",
            "China": "Beijing"}

capitals.update({"Germany": "Berlin"})

#print(capitals["UAS"])
#print(capitals.keys())
#print(capitals.get("Germany"))
#print(capitals.items())
#print(capitals.values())