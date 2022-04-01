# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification time)

import shutil
import os

shutil.copyfile("test.txt", "copy.txt")
shutil.copy("test.txt", "E:\\PyCharm Projects\\copy file.txt")


source = "text.txt"
destination = "E:\\PyCharm Projects\\text.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source + " was moved")
except FileNotFoundError:
    print(source + "was not find")

