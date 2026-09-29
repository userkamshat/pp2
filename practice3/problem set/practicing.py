m=int(input())
def factorial(n):
    factory=1
    for i in range(1,n+1):
        factory*=i
    return factory
print(factorial(m))
