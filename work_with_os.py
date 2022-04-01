import os
import shutil

path = "E:\\PyCharm Projects\\Text.txt"

if os.path.exists(path):
    print("That location exist!")
    if os.path.isfile(path):
        print("That is a file!")
    elif os.path.isdir(path):
        print("That is a directory!")
else:
    print("That location doesn't exist")

print("==============================")
try:
    with open("test.txt") as file:
        print(file.read())
except FileNotFoundError:
    print(FileNotFoundError)

print("================================")
text = "This is my text for file test.txt"
with open("test.txt", "a") as file:  # "a" append to a file, "w" write in file but all will be clear before
    file.write(text)

path = "FileForDelete.txt"

try:
    #  os.remove(path)   #delete a file
    #  os.rmdir(path)    #delete an empty directory
    shutil.rmtree(path)  # delete a directory containing files
except FileNotFoundError:
    print("File was not found.")
except PermissionError:
    print("You do not have permission to delete is.")
except OSError:
    print("You can`t delete it using that function.")
else:
    print(f"{path} was deleted!")
