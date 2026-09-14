x=5
y="John"
print(x)
print(y)
a=4
a="Sally"
print(a)
x=str(3)
y=int(3)
z=float(3)
print(x,y,z)
b=5
c="John"
print(type(b))
print(type(c))
x="John"
x1='John'
print(x==x1) #true
a=4
A="Sally"
print(a,A)
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()
print("Python is " + x)


def myfunc():
  global x
  x="fantastic"
myfunc()
print("Python is "+ x)