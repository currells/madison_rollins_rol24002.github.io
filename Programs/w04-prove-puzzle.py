"""
    Madison Rollins 
   W04 Prove Assignment: Word Puzzle
        I added a large word bank that is randomly selected, inclueded a promt 
    to ask if the user was ready, and a prompt to ask if the user wanted to play
    afian.  I used AI to help me correct areas of my code that were stumping me
    and to generat the list of words.  To learrn how to formulate the random word
    function I used an online python page.
"""
"""
#title
print(""
___________

      HI PALL!  WELCOME TO SHIKI'S CRAZY WORD GUEESER!

                    °˖✧◝(⁰▿⁰)◜✧˖°  
      
        I have thought of a super awsome 8 letter
        word and it's your job to guess what it is!
      
      You get INFINATE GUESSES!!!! :   ⊹⋛⋋( ՞ਊ ՞)⋌⋚⊹
___________
"")
#ready fready?
print()
ready = input ('Are you ready?: ')
#if no loop
if ready.lower() == 'no':
    print()
    ready = input ('Are you ready?: ')
#yes to start
else: 
    print()
    print('YAY!   °˖✧◝(⁰▿⁰)◜✧˖° ')
    print()
    print()
    #da word
    word = 'frazzled'
    count = 0
    #display enitial
    print('Your word is! : _ _ _ _ _ _ _ _')
    #Enter Guess
    guess = input('What word is it? (○´ ― `)ゞ  ')
    while word != guess.lower():
        print()
        print('Sorry, that is not the word. (っ˘̩╭╮˘̩)っ Try again: ')
        guess= input('What word is it? (○´ ― `)ゞ  ')
        count = (count + 1)
    print()
    print(f'YAY!   °˖✧◝(⁰▿⁰)◜✧˖°  You guessed it! The word was {word.upper()}!')
    print()
    print(f'You guessed it in {count} tries! ⊹⋛⋋( ՞ਊ ՞)⋌⋚⊹ ')
    play_again = input("Would you like to play again? づ ◕‿◕ )づ (yes or no): ")
    if play_again.lower() == "yes":
        return play_again
    else:
        print("(っ˘̩╭╮˘̩)っ Okay, bye by for now...Thanks for playing!")
"""

    

print("""___________

      HI PALL!  WELCOME TO SHIKI'S CRAZY WORD GUEESER!

                    °˖✧◝(⁰▿⁰)◜✧˖°  

        I have thought of a super awsome word and..
      it's your job to guess what it is!
                 
                 ⊹⋛⋋( ՞ਊ ՞)⋌⋚⊹
___________
""")
print()
print("""====== How to Play ======:
          ~ Enter a gues that has the
          same # of letters as 
          my chosen word!
          ~ "_" means the letter is 
          not in the word.
          ~ Lowercase letters mean the
          letter is in the word but 
          are not in that spot.
          ~ Upercase letters mean the 
          letter is in the right spot.
    """)
#ready fready?
print()
ready = input ('Are you ready?: ')
#if no loop
if ready.lower() != 'yes':
    print()
    ready = input ('Are you ready?: ')
#yes to start
else: 
    print()
    print('YAY!   °˖✧◝(⁰▿⁰)◜✧˖° ')
    print()
  #da word
    import random
    WORDS = ("apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew",
    "kiwi", "lemon", "lime", "mango", "nectarine", "orange", "papaya", "quince", "raspberry",
    "strawberry", "tangerine", "watermelon", "candy", "chocolate", "lollipop", "gumdrop", "gummy", 
    "caramel", "fudge", "nougat", "taffy", "truffle", "bonbon", "marshmallow", "cotton", "sugar", 
    "sweet", "sour", "bitter", "salty", "spicy", "flavor","kawaii", "cute", "fluffy", "pastel", 
    "heart", "star", "bunny", "kitty", "panda", "puppy", "fox", "raccoon", "dango", "mochi", "neko", 
    "usagi", "kawaii desu", "baka", "desu", "arigatō", "kudasai")
def play_game():
    word = random.choice(WORDS)
    count = 1
    for index in range(len(word)):
        letter = word[index]
        
#display enitial
    print('Here is my word! づ ◕‿◕ )づ ')
    for _ in range(len(word)):
        print('_ ', end="")
    print()
    print()
    #enter Guess
    guess = input('What word is it? (○´ ― `)ゞ  ')
    while  guess.lower() != word:
        count = (count + 1)
        if len(guess) != len(word):
                print(f'I am so sorry, THAT is not a {len(word)} letter word. ༽◺_◿༼  Please try again.')
                guess = input('What word is it? (○´ ― `)ゞ  ')
        else:
            for i in range(len(word)):
                letter = word[i]
                guess_letter = guess.lower()[i]
                if letter.lower() == guess_letter:
                    print(letter.upper(), end=" ")
                elif guess_letter in word:
                     print(guess_letter.lower(), end=" ")
                else:
                     print('_ ', end="")
            print()

            if guess.lower() != word:
                print("That's not quite right. Try again!")

        guess = input('What word is it? (○´ ― `)ゞ  ')
#while loop end    
    print(f'YAY!   °˖✧◝(⁰▿⁰)◜✧˖°  You guessed it! The word was {word.upper()}!')
    print()
    print(f'You guessed {word.upper()} in {count} tries! ᕙ(‾̀◡‾́)ᕗ ')
    print()
    play_again = input("Would you like to play again? (yes/no): ").lower() == "yes"
    return play_again
play_again = True
while play_again:
    play_again = play_game()
print("(っ˘̩╭╮˘̩)っ Okay, bye by for now...Thanks for playing!")

"""for letter in word:
        if range(len(guess)) != range(len(word)):
            print('I am so sorry, THAT is not an 8 letter word. ༽◺_◿༼  Please try again.')
            guess = input('What word is it? (○´ ― `)ゞ  ')
        elif letter == word[index]:
            print(letter.upper(), end="")
        else:
           print('_', end="")
           guess = input('What word is it? (○´ ― `)ゞ  ')"""
    
#Enter Guess
"""guess = input('What word is it? (○´ ― `)ゞ  ')
    for letter in word:
        if letter.lower() == guess.lower():
            print(letter.upper(), end="")
        #elif letter.lower() == 
    else:
       guess = input('What word is it? (○´ ― `)ゞ  ')
"""