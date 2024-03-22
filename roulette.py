import random
from colorama import Fore, Style, Back

def Play():
    print(Fore.WHITE + Style.BRIGHT + 'Welcome, Please select your number from 0 to 36')
    
    number = random.randint(0,36)
    selectNum = input()

    if int(selectNum) > 36:
        print(Fore.BLUE + Style.BRIGHT + 'Invalid number entered')

    elif int(selectNum) == number:
        number = str(number)
        print(Fore.GREEN + Style.BRIGHT + 'You Won! The winning number is ' + number)

    elif int(selectNum) != number:
        number = str(number)
        print(Fore.RED + Style.BRIGHT + 'You Lost! The winning number is ' + number)

Retry = 'Yes'
while Retry == 'Yes' or Retry == 'y':
    Play()

    print(Fore.WHITE + Style.BRIGHT + 'Do you want to play again ? (Yes or No)')
    Retry = input()
