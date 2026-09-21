def unique_elements(numbers):

    result = []

    for n in numbers:
        if n not in result:
            result.append(n)

    return result


print(unique_elements([1, 2, 2, 3, 4, 4, 5]))