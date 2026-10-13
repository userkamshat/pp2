with open("demofile.txt","w") as file:
    file.write("Hello, Python!\n")
    file.write("This is Practice 6.\n")

with open("demofile.txt","a") as file:
    file.write("This line was added later.\n")
print("File created and updated.")


