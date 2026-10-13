import os
import string
import shutil
print("1. List directories and files")
print("2. Check path access")
print("3. Get filename and directory")
print("4. Count file lines")
print("5. Write a list to a file")
print("6. Create A.txt to Z.txt")
print("7. Copy file contents")
print("8. Delete a file safely")

choice = input("Choose exercise (1-8): ")
if choice=="1":
    path=input("Enter directory path: ")
    if os.path.isdir(path):
        print("Directories:")
        for name in os.listdir(path):
            if os.path.isdir(os.path.join(path,name)):
                print(name)
        print("All contents:",os.listdir(path))
    else:
        print("Directory does not exist")

elif choice=="2":
    path=input("Enter path: ")
    print("Exists:",os.path.exists(path))
    print("Readable:",os.access(path,os.R_OK))
    print("Writable:",os.access(path,os.W_OK))
    print("Executable:",os.access(path,os.X_OK))

elif choice=="3":
    path=input("Enter path: ")

    if os.path.exists(path):
        print("Filename:",os.path.basename(path))
        print("Directory:",os.path.dirname(path))
    else:
        print("Path does not exist")

elif choice=="4":
    path=input("Enter text file path: ")
    if os.path.isfile(path):
        with open(path,"r") as file:
            print("Number of lines:",len(file.readlines()))
    else:
        print("File does not exist")

elif choice=="5":
    items=["Apple","Banana","Orange"]
    with open("list.txt","w") as file:
        for item in items:
            file.write(item + "\n")
    print("List written to list.txt")

elif choice=="6":
    for letter in string.ascii_uppercase:
        with open(letter+ ".txt","w") as file:
            file.write(letter)
    print("Created 26 files")

elif choice == "7":
    source = input("Enter source file: ")
    destination = input("Enter destination file: ")

    if os.path.isfile(source):
        shutil.copyfile(source, destination)
        print("File copied")
    else:
        print("Source file does not exist")

elif choice == "8":
    path = input("Enter file path to delete: ")

    if os.path.isfile(path):
        if os.access(path, os.W_OK):
            try:
                os.remove(path)
                print("File deleted")
            except OSError as error:
                print("Error:", error)
        else:
            print("File is not writable")
    else:
        print("File does not exist or is not a file")

else:
    print("Invalid choice")