import random

def checkGuess(secret, guess):

    if secret == guess:
        result = 0
    elif secret > guess:
        result = 1
    else:
        result = -1
    
    return result

# optional code to check proper input ##############
def check_for_integer(inpt):
    is_wrong_input = True

    while is_wrong_input:
        
        try:
            inpt = int(inpt)
            break
        except:
            inpt = input("That's not integer. Try again: ")     
    return inpt