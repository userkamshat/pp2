def reverse_words(sentence):
    words = sentence.split()
    words.reverse()

    return " ".join(words)


text = input("Enter a sentence: ")

print(reverse_words(text))