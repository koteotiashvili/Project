# firstly we need to import random to randomize number to guess
import random


# after that we need to define a function
def guess_number():
    # use from random randint to chose number from 1 to 10
    number = random.randint(1, 10)
    # define number of attempts user have
    attempt = 6
    # use while to creat loop
    guessed = False
