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

    while not guessed and attempt > 0:
        try:
            # after that we just use if elif else to give statement to our code
            guess = int(input("Guess a number between 1 and 10: "))
            if guess == number:
                print(f"Congratulations! You won, You guessed {number}!!")
                guessed = True
            # use elif statement to give our code function if user guessed number wrong they lose attempt
            elif guess > number:
                print(f'number is lower than {guess}, u have: {attempt - 1} tries left')
                attempt -= 1
            elif guess < number:
                print(f'number is higher than {guess}, u have: {attempt - 1} tries left')
                attempt -= 1
            # and use except  to Value our error if user will not put number
        except ValueError:
            print(f"You must use a number, u have {attempt - 1} tries left")
            attempt -= 1
        if not guessed:
            print(f'you ran out of attempts, u lost,number was {number}')


guess_number()
