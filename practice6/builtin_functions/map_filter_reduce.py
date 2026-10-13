from functools import reduce
numbers=[1,2,3,4,5]
print(len(numbers))
print(sum(numbers))
print(min(numbers))
print(max(numbers))
print(sorted(numbers))
squares=list(map(lambda x:x*x,numbers))
print(squares)
even=list(filter(lambda x:x%2==0,numbers))
print(even)
total=reduce(lambda x,y:x+y,numbers)