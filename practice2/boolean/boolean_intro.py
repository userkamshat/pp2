print(10 > 9) #true
print(10 == 9) #false
print(10 < 9) #false

"""
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a") #<--result
"""

print(bool("Hello"))#true
print(bool(15))#true
#FALSE:
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))

#true:
def myFunction() :
  return True

print(myFunction())

def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")


x = 200
print(isinstance(x, int)) #-->true