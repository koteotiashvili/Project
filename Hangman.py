# Use import random to randomize chosen word
import random


# Define chosen word and randomize it
def choose_word():
    word_list = ['apple', 'banana', 'cherry', 'dog', 'cat', 'wolf' 'bee', 'orange']
    return random.choice(word_list)


# Define display words with if else statements
def display_word(word, guessed_letters):
    # Display the word with blank for letters not guessed yet
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter

        else:
            # Display the word with _ for letters not guessed yet
            displayed_word += "_"
    return displayed_word


# Define game and secret word and attempts
def hangman():
    print("Welcome to Hangman!")
    secret_word = choose_word()
    guessed_letters = []
    attempts = 6
    # use while to create loop and if attempts will be equal 0 loop will stop
    while attempts > 0:
        # print how many attempts are left
        print("\nAttempts left:", attempts)
        # print how many secret and how many guessed letters are left
        print("Word:", display_word(secret_word, guessed_letters))
        # use input to put letter and .lower to convert any uppercase letter to lowercase
        guess = input("Guess a letter: ").lower()
        # use if to make a statement that letter must be single length and must be alphabet
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            # use statement so if user tries to guess same letter console will tell hin that he already guessed that letter
        elif guess in guessed_letters:
            print("You've already guessed that letter.")
            # use append to keep tracking what letters user used
            guessed_letters.append(guess)

            # use if not in to highlight incorrect guesses
            if guess not in secret_word:
                attempts -= 1
                print("Incorrect guess!")
            # and use if not to check if - is in word if not in it means user won game
            if "_" not in display_word(secret_word, guessed_letters):
                print("\nCongratulations! You guessed the word:", secret_word)
                break
hangman()

