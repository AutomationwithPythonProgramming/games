import random
from colorama import Fore

def Play():
    print(Fore.WHITE + 'Welcome, Please select your number from 0 to 36')
    
    number = random.randint(0,36)
    selectNum = input()

    if int(selectNum) > 36:
        print(Fore.BLUE + 'Invalid number entered')

    elif int(selectNum) == number:
        number = str(number)
        print(Fore.GREEN + 'You Won! The winning number is ' + number)

    elif int(selectNum) != number:
        number = str(number)
        print(Fore.RED + 'You Lost! The winning number is ' + number)

Retry = 'Yes'
while Retry == 'Yes':
    Play()

    print(Fore.WHITE + 'Do you want to play again ? (Yes or No)')
    Retry = input()
