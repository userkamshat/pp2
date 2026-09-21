def is_palindrome(word):

    word = word.lower()

    if word == word[::-1]:
        return True
    else:
        return False


text = input("Enter a word: ")

print(is_palindrome(text))