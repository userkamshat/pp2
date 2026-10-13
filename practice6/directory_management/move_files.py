import os
import shutil

os.makedirs("folder1", exist_ok=True)
os.makedirs("folder2", exist_ok=True)

with open("folder1/example.txt", "w") as file:
    file.write("Example text")

shutil.copy("folder1/example.txt", "folder2/example.txt")
print("File copied.")

shutil.move("folder1/example.txt", "folder2/example_moved.txt")
print("File moved.")