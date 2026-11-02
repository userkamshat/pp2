import os
shopping=["milk","bread","tovar1","tovar2","tovar3"]
os.mkdir("myfolder3")
with open("myfolder3/shopping.txt","w") as file:
    for item in shopping:
        file.write(item+"\n")
with open("myfolder3/shopping.txt","r")as file:
    items=file.readlines()
print("shopping lists:")
for i in range(len(items)):
    print(i+1,items[i].strip())

with open("myfolder3/shopping.txt","a") as file:
    file.write("cheese")
    file.write("banana")

with open("myfolder3/shopping.txt","r") as file:
    items=file.readlines()
items.sort()

with open("myfolder3/shopping_sorted.txt","w") as file:
    for item in items:
        file.write(item)