#create qrcode
''''import qrcode
img = qrcode.make("Shemaya is the greatest ever to have ever lived")#here input what the qr code outputs
img.save("youtubeQR.jpg")'''''

#rolling dice

import random
min = 1
max = 6

roll_dice = input("do you  want to roll again? (y  or yes) ")  #roll_again == "yes" or roll_again == "y"

if roll_dice == "y" or "yes":
    print(random.randint(min, max))
elif roll_dice != "y" or "yes":
    print("invalid")
else:
    print("dumbass!!!!")

#guess number
''''import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')

    print(f'Yay, congrats. You have guessed the number {random_number} correctly!!')
#Guess number

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
            feedback = input(f'Is{guess} too high(H), too low(L), or correct(C)??').lower()
        if feedback == h:
            high = guess -1
        elif feedback == '1':
            low = guess + 1
    print(f'the computer guessed your number, {guess}, correctly')'''''



