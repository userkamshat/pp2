names=["Anna","Dana","Ali"]
ages=[18,19,20]
print("Enumerate:")
for index,name in enumerate(names):
    print(index,name)

print("Zip:")
for name,age in zip(names,ages):
    print(name,age)