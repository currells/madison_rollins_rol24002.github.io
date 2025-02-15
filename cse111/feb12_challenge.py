import pytest
#Write 1 while loop w/4 if/eslse statmets multiple returns and does math operations."""
# defining variables

#class
print("Grade Calculator")
print()
print("Enter 'quit' to end the program.")
print()

course = input("Enter Class: ")

print()
#grade percentage
num = float(input("Enter Grade Percent: "))

while course.lower != "quit": 
    #if statement numbers
    if num >= 90:
        grade = "A"
    elif num >= 80:
        grade = "B"
    elif num >= 70:
        grade = "C"
    elif num >= 60:
        grade = "D"
    else:
        grade = "F"
    #if sign
        sign=""
    last_digit = grade % 10
    if last_digit >= 7:
        sign="+"
    elif last_digit < 3:
        sign = "-"
    else:
        sign=""
#printing grades
print()
print(f"Your Grade Letter is: {grade.capitalize()}{sign}")
