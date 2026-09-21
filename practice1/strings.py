a = "Hello, World!"
print(a[1]) #e
for x in "banana":
  print(x)
a = "Hello, World!"
print(len(a))
txt = "The best things in life are free!"
print("free" in txt)
txt = "The best things in life are free!"
if "free" in txt:
  print("Yes, 'free' is present.")
txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


b = "Hello, World!"
print(b[2:5])
b = "Hello, World!"
print(b[:5])
b = "Hello, World!"
print(b[2:])
b = "Hello, World!"
print(b[-5:-2]) #orl

a = "Hello, World!"
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("H", "J"))
print(a.split(","))
a = "Hello"
b = "World"
c = a + " " + b
print(c)
age=36
txt=f"my name is john,i am {age}"
print (txt)
price = 59
txt = f"The price is {price} dollars"
print(txt)

txt=f"The price is {price} dollars"
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

price=59
txt=f"The price is {price:.2f} dollars" #59.00
#7.02,after point 2 symb

txt = f"The price is {20 * 59} dollars"
print(txt)
txt = "We are the so-called \"Vikings\" from the north."#\"\"
txt="Hello, World!"
print(txt[2:5])
print(txt.upper())
name="Python"
print(f"I love {name}")