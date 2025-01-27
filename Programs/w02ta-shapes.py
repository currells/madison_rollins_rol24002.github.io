"""
    Madison Rollins
    Team Activity: Shapes
"""

import math
#Reece Code I made look pretty
print()
print('-----------')
print()
print('Calculate Square Area and Volume')
#input
print()
print('-----------')
side = float(input("What is the length of a side of the square? "))
#math
sarea = (side ** 2)
svolume = (side **3)
print()
#display area
print(f'The Area of the square is: {sarea: .2f}')
print(f'The Volume of the cube is: {svolume: .2f}')
print()
print('-----------')
print()
#rectangele
print()
print('-----------')
print()
print('Calculate Rectangele Area')
#inputs
print()
print('-----------')
l = input('Length of rectangle:')
w = input('Width of rectangle:')
#math
rarea = (float(l) * float(w))
print()
#display area
print(f'The area of the rectangle is: {rarea: .2f}')
print('-----------')

#Samantha Circle calculatops
print()
print('-----------')
print()
print('Calculate Circle Area')
#inputs
print()
print('-----------')
print()
circle_radius=float(input(f"What is the radius of the circle?"))
print()
circle_area=3.14 * (circle_radius**2)
circle_volume= ((4/3) * 3.14 * ((circle_radius)**3))
print()
print(f"The area of the circle is: {circle_area:.2f}")
print(f"The Volume of the circle is: {circle_volume:.2f}")
print()
print('-----------')
print()