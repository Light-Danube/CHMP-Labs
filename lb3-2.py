import math
import numpy as np
from scipy.misc import derivative

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

def CombinedMethod(a,b,eps):
    if (derivative(f, a, n = 1)*derivative(f, a, n = 2)>0):
        a0 = a
        b0 = b
       
    else:
        a0 = b
        b0 = a
    ai = a0
    bi = b0
    while abs(ai-bi)>eps:   
        ai_1 = ai -f(ai)*(bi - ai)/(f(bi) - f(ai))
        bi_1 = bi - f(bi)/derivative(f,bi, n= 1) 
        ai = ai_1
        bi = bi_1
    x = (ai_1+bi_1)/2 
 
    return print('Solving the equation by the combined method x = ', round(x, 4))

CombinedMethod(-1,0,eps)
CombinedMethod(1,2,eps)
