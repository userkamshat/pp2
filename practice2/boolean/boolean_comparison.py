x = 5
y = 3
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

x = 5
print(1 < x < 10)
print(1 < x and x < 10)
print(x > 0 and x < 10)
print(x < 5 or x > 10)
print(not(x > 3 and x < 10))

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x == y)
print(x is not y)

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)
print(x is y)
#is - Checks if both variables point to the same object


fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)
print("pineapple" not in fruits)

text = "Hello World"
print("H" in text)
print("hello" in text)
print("z" not in text)

print(6 & 3)
print(6 | 3)
print(6 ^ 3)
print((6 + 3) - (6 + 3))
print(100 + 5 * 3)
print(5 + 4 - 7 + 3)

a=15
b=4
print(a%b) #modulus
print(a//b) #floor division
print(a**b) #power of
a+=10
