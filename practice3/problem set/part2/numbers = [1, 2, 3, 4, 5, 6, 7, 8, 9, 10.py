numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def is_prime(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


result = list(filter(lambda x: is_prime(x), numbers))

print(result)



def is_palindrome(word):
    word=word.lower()
    if word==word[::-1]:
        return True
    else:
        return False
    
text=input("Enter the word: ")
print(is_palindrome(text))


def histogram(numbers):
    for n in numbers:
        print("*"*n)


histogram([4,9,7])