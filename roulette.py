import random

def Play():
    print('Welcome, Please select your number from 0 to 36')

    number = random.randint(0,36)
    selectNum = input()

    if int(selectNum) > 36:
        print('Invalid, re-enter number from 0 to 36')

    elif int(selectNum) == number:
        number = str(number)
        print('You Won! The winning number is ' + number)

    elif int(selectNum) != number:
        number = str(number)
        print('You Lost! The winning number is ' + number)

Retry = 'Yes'
while Retry == 'Yes':
    Play()

    print('Do you want to play again ? (Yes or No)')
    Retry = input()
