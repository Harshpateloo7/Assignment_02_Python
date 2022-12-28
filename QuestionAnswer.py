import random

# get a random integer between 97 and 122
# The reason for using 97 to 122 is we can use in-built 'chr' function and convert it to letter
computer_guess = chr(random.randint(97,122))
print('computer guess:',computer_guess)   #REMOVE THIS LINE BEFORE SUBMITTING

#print welcome message
print('-'*50)
print('Welcome to the Game!')
print('Guess any letter between A to Z.')
print('If you guess is correct first time you will get 26 pts, if your guess correct second time you will get 13 pts and if your guess correct second time you will get 7 pts.')
print('-'*50)


#sanatize user input
def clean_userinput(user_input):
    is_wrong_input = True
    
    while is_wrong_input:
        user_input = user_input.lower()
    
        if len(user_input) > 1:
            user_input = input('You have entered more than one letter. Try again: ')
        
        elif not user_input.isalpha():
            user_input = input('You can only enter single letters. Try again: ')
            
        else:
            break
    
    return user_input

def score_calculator(game_counter):

    if game_counter == 0:
        return 26
    elif game_counter == 1:
        return 13
    elif game_counter == 2:
        return 7
    else:
        return 0

def checkSum(user_input, computer_guess):
    
    if ord(user_input) > ord(computer_guess):
        return 'Your guess is too high.'

    elif ord(user_input) < ord(computer_guess):
        return 'Your guess is too low'

    else:
        return 'correct'

def allow_retry(inpt):

    if inpt.lower() == 'r':
        allowed_attempts = 0

#count number of attempt and allowed attempts
allowed_attempts = 3
actual_attempts = 0

#create a varible to capture a score:
score = 0

while actual_attempts < allowed_attempts:
    #print('actual attemps:', actual_attempts)
    if actual_attempts == 0:
        user_input = clean_userinput(input("Guess a letter: "))
    
    else:
        print('-'*50)
        user_input = clean_userinput(input('Guess another letter: '))

    answer = checkSum(user_input, computer_guess)

    if answer == 'correct':
            print('-'*50)
            print('Your guess is correct')
            score = score_calculator(actual_attempts)
            print(f"Your Score is: {score} ")
            print('-'*50)
            break

    else:
        print(answer)


    
    actual_attempts +=1

    if actual_attempts == 3:
        print('-'*50)
        user_input = input('Enter "r" to retry OR any other key to exit: ')

        if user_input.lower() == 'r':
            actual_attempts = 0
        else:
            print('Thank you for playing!')
            break




