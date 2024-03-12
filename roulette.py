import random

number = random.randint(0,36)
print('Welcome, Please select your number from 0 to 36')

selectNum = input()
# selectNum = int(selectNum)

if int(selectNum) > 36:
    print('Invalid, re-enter number from 0 to 36')

elif int(selectNum) == number:
    number = str(number)
    print('You Won! The winning number is ' + number)

elif int(selectNum) != number:
    number = str(number)
    print('You Lost! The winning number is ' + number)
