import random

def choose_word():
    words = ["apple", "banana", "orange", "grape", "strawberry"]
    return random.choice(words)

def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "_"
    return displayed_word

def hangman():
    word = choose_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print("Try to guess the word.")

    while True:
        print("\n" + display_word(word, guessed_letters))

        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in word:
            print("Incorrect guess!")
            incorrect_guesses += 1
            print(f"You have {max_incorrect_guesses - incorrect_guesses} guesses left.")
            if incorrect_guesses >= max_incorrect_guesses:
                print("Sorry, you lose! The word was:", word)
                break
        else:
            if "_" not in display_word(word, guessed_letters):
                print("Congratulations, you win! You guessed the word:", word)
                break

hangman()