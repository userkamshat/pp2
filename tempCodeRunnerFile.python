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