def filter_prime(numbers):

    result = []

    for n in numbers:
        if n < 2:
            continue

        prime = True

        for i in range(2, n):
            if n % i == 0:
                prime = False
                break

        if prime:
            result.append(n)

    return result


numbers = list(map(int, input().split()))

print(filter_prime(numbers))