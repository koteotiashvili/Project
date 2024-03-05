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


