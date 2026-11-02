import os

os.mkdir("myfolder")

with open("myfolder/database.ini", "w") as file:
    file.write("Hello")