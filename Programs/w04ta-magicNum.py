"""
    Madison Rollins
Guess the magic Number!!
        I did not meet with my team bbut completed the activity on my own
"""
#imports 
import random

number = random.randint(1,10)

#title
print('GUESS THE MAGIC NUMBER between 1-10')
print()
print()
#input
guess = int(input('What is the magic number?  '))
print()
count = 0
while guess != number:
    count = count + 1
    guess = int(input('What is the magic number?  '))
    print()

    if guess > number:
        print('Guess a lower number') 
    elif guess < number: 
        print('Guess a higher number')
    else:
        print(f'You got it!! You guest the magic number was {number} in {count} tries!') 
        print()
        play = input('Would you like to play again? (yes or no)')
if play.lower == 'yes':
    print()
    guess = int(input('What is the magic number?  '))
else:
    print('No problem!  Thanks for playing!')