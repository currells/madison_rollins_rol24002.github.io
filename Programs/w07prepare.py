"""
    Madison Rollins W07 Prepare
    Write three functions:

display_regular—Receives a string and prints it out, exactly as received.

display_uppercase—Receives a string, converts it to upper case, and then prints it out.

display_lowercase—Receives a string, converts it to lower case, and then prints it out.

In your program below the functions, ask the user to type a message. Then, pass that message to each of the three functions, so it it displays it each way, as shown:


What is your message? I can do all things through Christ
I can do all things through Christ
I CAN DO ALL THINGS THROUGH CHRIST
i can do all things through christ
Another example is:


What is your message? The only thing we have to fear is FEAR itself!
The only thing we have to fear is FEAR itself!
THE ONLY THING WE HAVE TO FEAR IS FEAR ITSELF!
the only thing we have to fear is fear itself!
"""

"""
#input
message = input('What is your message?: ')
def display_regular():
    print(message)
def display_uppercase():
    print(message.upper())
def display_lowercase():
    print(message.lower())
display_regular()
display_uppercase()
display_lowercase()

"""




"""
Write a function compute_area_square that accepts a single value as a parameter, and then computes the area and returns it.

Below the function, write code to prompt the user for the side of a square and save it into a variable, then pass this variable to the function to compute the area. Finally, get the result back from the function and display it.

Repeat the previous step to write and test the functions compute_area_rectangle and compute_area_circle.

Write a loop to ask the user what kind of shape they have, then prompt for the length of a side, or sides, or radius, and then calls the appropriate function, and displays the result. The program should continue looping until the user enters "quit" for the shape.

Recognize that you can compute the area of a square by passing the task along to a function that computes the areas of rectangles, by giving it the side of the square twice.

Change your program so that the compute_area_square function doesn't compute the area directly, but instead calls the compute_area_rectangle to do the work. It should pass the square side length to it (twice) and then return the value that the compute_area_rectangle function computes.

"""

"""
import math
#defining functions
def compute_area_square(side):
    return side * side
 

def compute_area_rectangle(length, width):
    return length * width

def compute_area_circle(radius):
    return 3.14 * (radius**2)
#What Shape
shape=""

while shape != "quit":
    shape = input("What shape do you have? ")
    shape = shape.lower()
    #if statements
    
    #SQUARE
    if shape == 'square':
       print()
       print('-----------')
       print()
       print('Calculate Square Area and Volume')
       #input
       print()
       print('-----------')
       side = float(input("What is the length of a side of the square? "))
       #area
       sarea = compute_area_square(side)
       print(f'The Area of the square is: {sarea: .2f}')

    #rectangle
    if shape == 'rectangle':
        print('-----------')
        print()
        print('Calculate Rectangele Area')
        #inputs
        print()
        print('-----------')
        length = float(input('Length of rectangle:'))
        width = float(input('Width of rectangle:'))
        #area
        rarea = compute_area_rectangle(length, width)
        print(f'The Area of the rectangle is: {rarea: .2f}')
    
    #circle
    if shape == 'circle':
        print()
        print('-----------')
        print()
        print('Calculate Circle Area')
        #inputs
        print()
        print('-----------')
        print()
        radius = float(input(f"What is the radius of the circle?"))
        print()
        carea = compute_area_circle(radius)
        print()
        print(f"The area of the circle is: {carea:.2f}")
print('Thank you.')
"""
def display_numbers(x, y):
    return 10

x = 3
y = 4
x = display_numbers(x, y)

print(x)