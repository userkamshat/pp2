with open("demofile.txt","r") as file:
    print("READ ALL:")
    print(file.read())

with open("demofile.txt","r") as file:
    print("Read one line:")
    print(file.readline())

with open("demofile.txt","r")as file:
    print("Read lines:")
    print(file.readlines())