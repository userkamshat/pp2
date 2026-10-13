import os
from pathlib import Path

os.makedirs("myfolder/subfolder", exist_ok=True)

print("Current directory:", os.getcwd())
print("All items:", os.listdir("."))

print("Directories:")
for name in os.listdir("."):
    if os.path.isdir(name):
        print(name)

print("Text files:")
for name in os.listdir("."):
    if os.path.isfile(name) and name.endswith(".txt"):
        print(name)

folder = Path("myfolder")
print("Folder exists:", folder.exists())