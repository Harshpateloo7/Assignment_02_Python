# I Harshadkumar_Patel, 000852665, certify that this work is my own effort and that I have not allowed anyone else to copy from it.
import random

#Question 1: Answer 1
def checkGuess(secret, guess):

    if secret == guess:
        result = 0
    elif secret > guess:
        result = 1
    else:
        result = -1
    
    return result

# optional code to check proper input:
def check_for_integer(inpt):
    is_wrong_input = True

    while is_wrong_input:
        
        try:
            inpt = int(inpt)
            break
        except:
            inpt = input("That's not integer. Try again: ")     
    return inpt
    
# Question 2: Answer 2
def main():

    #get a username from user input
    username = input('What is your name: ')

    # create a random interger using username lenght and random integer
    secret_number = len(username) * random.randint(1,10)
    # set score and guesses
    score = 0
    guesses = 0
    # loop to check score and correct user input
    while True:

        remaining = 3 - guesses

        user_input = check_for_integer(input('Enter your integer guess: '))
        guesses = guesses + 1

        result = checkGuess(secret_number, user_input)

        if result == 0:
            if guesses == 1:
                print('Amazing! On your first guess!')
                score = score + 10
            else:
                if guesses == 2:
                    print('Excellent! On your second guess!')
                    score = score + 5
                else:
                    print('Lucky! On your last guess!')
                    score = score + 1
            break
        else:
            if result ==1:
                print(f'Your guess, {guesses}, was too low!')
            else:
                print(f'Your guess, {guesses}, was too high!')

        if guesses == 3:
            break

    print(f'Thank you for playing, {username}, your score was {score}')


# execure main module to play a game
if __name__ == "__main__":
    main()


