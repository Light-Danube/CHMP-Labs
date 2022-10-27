import math
import numpy as np
from scipy.misc import derivative
from scipy import optimize

eps = 0.001

def f(x):
    return 3*pow(x, 4) - 4*pow(x, 3) + pow(x, 2) - 2*x - 3

def find_segments():
    search_range = np.arange(-10, 10, 1)
    
    c = None
    prev_x = None
    clue_x = None
    segments = []
    
    for x in search_range:
        x = round(x, 4)
        clue_x = f(x)
        if prev_x != None and prev_x * clue_x < 0:
            segments.append((c,x))
        c = x
        prev_x = clue_x
    
    return segments

segments = find_segments()
for a, b in segments:
    print(f'Seg:', [{a}, {b}])

def NewtonMethod(a, b, eps):
    
    df2 = derivative(f, b, n = 2)
    if (f(b) * df2 > 0):
        xi = b
    else:
        xi = a
        
    df = derivative(f, xi, n= 1)
    xi_1 = xi - (f(xi)/df)
    
    while (abs(xi_1 - xi)>eps): #accuracy check
        xi = xi_1
        xi_1 = xi - f(xi)/df
    return print ('Solving the equation by Newton method x = ', round(xi_1, 4))

NewtonMethod(-1,0,eps)
NewtonMethod(0,2,eps)