import random

words = ["apple", "mango", "banana", "peach"]
word = random.choice(words)
guessed = []
tries = 6

print("Welcome to Hangman Game")

while tries > 0:
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"

    print("Word:", display)

    if display == word:
        print("🎉 You win!")
        break

    guess = input("Guess a letter: ").lower()

    if guess in guessed:
        print("You already guessed that letter!")
        continue

    guessed.append(guess)

    if guess in word:
        print("✅ Good guess!")
    else:
        tries -= 1
        print("❌ Wrong guess! Tries left:", tries)

else:
    print("😢 You lost! The word was:", word)
