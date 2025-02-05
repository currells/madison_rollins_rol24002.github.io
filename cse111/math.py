"""Implimenting sigma(x) = 1/1+e^-x"""
#Importing Math
import math
#defining function
def sigmoid(x):
    return 1/ (1 + math.exp(-x))

#defining quadratic formula
def solve_quadratic_equation(a, b, c):
    #descriminative
    descriminative = (b**2) - 4*(a*c)

    #the ohter things
    x1 = (-b - descriminative**0.5) / (2*a)
    x2 = (-b + descriminative**0.5) / (2*a)

    return x1, x2
#Kenetic Energy
def kenetic_energy(m, v):
    return .5 * m *(v + math.exp(2))

#force?
def gravital_foce(r, g, m, M):
    return g((m * M)/(r + math.exp(2)))

