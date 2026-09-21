import random


name = input("Hello! What is your name?\n")

number = random.randint(1, 20)

print("Well,", name + ", I am thinking of a number between 1 and 20.")

guesses = 0

while True:

    guess = int(input("Take a guess.\n"))
    guesses += 1

    if guess < number:
        print("Your guess is too low.")

    elif guess > number:
        print("Your guess is too high.")

    else:
        print("Good job,", name + "!")
        print("You guessed my number in", guesses, "guesses!")
        break