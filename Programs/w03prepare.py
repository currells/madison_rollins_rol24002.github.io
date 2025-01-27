#If Statment and Else statements
print("Please Enter the following")
"""
Comparing Strings
Have the program ask the user for their favorite animal. Then write an if statement as follows:

Check to see if the user's favorite animal is the same as your favorite animal
(meaning you, the programmer). If it is, print "That's my favorite animal too!" 
If it's not, print "That one is not my favorite." 
Verify that it works regardless of the capitalization."""
print()
print()
print("----------")
print()
print("Comparing Strings")
print()
print()
print("----------")
print()
#String input
favani = input("What is your favorite animal?")
#if statement 
if  favani.lower() == "fox":
    print("YAY!!!!  I LOVE Foxes too!")
#else statement
else:
    print("Bummer! That's not my favorite animal!")
print()
print("----------")
print()









"""
Write a program that asks the user for two integers.

Then, write three separate if/else statements as follows:

If the first number is greater than the second, 
print "The first number is greater". Otherwise, 
print "The first number is not greater".

If the two numbers are equal print "The numbers are equal".
 Otherwise, print "The numbers are not equal".

If the second number is greater than the first, 
print "The second number is greater". Otherwise, 
print "The second number is not greater".
"""
print()
print()
print("----------")
print()
print("Comparing Numbers")
print()
#title
print("Please Enter Two Whole Numbers")
print()
#input one
one = int(input("First Number: "))
#input two
two = int(input("Second Number: "))
print()
print("----------")
print()
"""If the first number is greater than the second, 
print "The first number is greater". Otherwise, 
print "The first number is not greater"."""
#if statement 
if one > two:
    print("The first number is greater")
#else statement
else:
    print("The first number is not greater")
print()
print("----------")
print()
"""If the two numbers are equal print "The numbers are equal".
 Otherwise, print "The numbers are not equal"."""
# if statement
if one == two:
    print("The numbers are equal")
#else statement
else:
    print("The numbers are not equal")
print()
print("----------")
print()
"""If the second number is greater than the first, 
print "The second number is greater". Otherwise, 
print "The second number is not greater"."""
# if statement:)
if two > one:
    print("The second number is greater")
# else statement
else:
    print("The second number is not greater")
print()
print("----------")
print()
print("Thank You! :) ")


