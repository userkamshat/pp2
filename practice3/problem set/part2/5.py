from itertools import permutations


def all_permutations(text):

    result = permutations(text)

    for p in result:
        print("".join(p))


text = input("Enter a string: ")

all_permutations(text)