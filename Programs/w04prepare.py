"""
        Madison Rollins
      W04 Prepare Assignmet
"""

"""WHILE LOOPS  (: :)"""


"""
#NUMBER
num = float(input('Please type a positive number! :'))
#while statement
while num < 0:
    print('I am so sorry, THAT is a negative number. ༽◺_◿༼  Please try again.')
    num = float(input('Please type a positive number! :'))
#final print
print(f'Good Choice! ⊹⋛⋋( ՞ਊ ՞)⋌⋚⊹  Your number is {num: .2f}')
print()
print()
print()
candy = input('May I has a peice of cawndy? (づ ◕‿◕ )づ')
# while statemenenet
while candy != 'yes':
    print('(っ˘̩╭╮˘̩)っ')
    candy = input('May I has a peice of cawndy? (づ ◕‿◕ )づ')
print('⊹⋛⋋( ՞ਊ ՞)⋌⋚⊹ YAY!!! (っ˘ڡ˘ς) Thanks you!')

"""

"""
    FOR LOOP :0
"""

"""
print()
print('Hey, look! ( ๑‾̀◡‾́)σ"')
print()
#color thing
colors = ["red", "blue", "green", "yellow"]
#for
for item in colors:
    print(item)
print()
print('(ᵒ̤̑ ₀̑ ᵒ̤̑)wow!*✰ COLORS')

#numbers
print('WHAT ARE THOSE!?!?!  (○´ ― `)ゞ')
# what nums?
numbers = range(1, 9)
for numbers in  range(1, 9):
    print(numbers)

#more numbers count by 2
print('Watch me count by 2!  ᕙ(‾̀◡‾́)ᕗ')
#da range and comand
by2 = range(2, 21, 2)
for by2 in range(2, 21, 2):
    print(by2)
"""

"""
LOOPING THROUGH STRINGS :) -------- (:
"""
"""
#da word
word = "commitment"
#ask for favorite letter
favlet = input('What is your favorite letter?: ')
for letter in word:
    if letter.lower() == favlet.lower():
        print(letter.upper(), end="")
    else:
        print(letter.lower(), end="")

#omit
word = "commitment"
#ask for favorite letter
favlet = input('What is your favorite letter?: ')
for letter in word:
    if letter.lower() == favlet.lower():
        print('_', end="")
    else:
        int(letter.lower(), end="")
"""