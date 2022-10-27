import numpy as np
import math
from scipy import optimize

#sin(x+1) - y = 1
#2x + cos(y) = 2

e = 0.001
x0 = 0 #intial X guess
y0 = 0 #intial Y guess

def f1(x):
    return -1 + math.sin(x+1)

def f2(y):
    return 1 - math.cos(y) / 2

#Find our X0 & Y0 values:
def simpleIterationMethod(x, y, e):
    xn = x
    yn = y
    xn1 = f1(x)
    yn1 = f2(y)
    n = 1
    while ((abs(xn1-xn)>=e) & (abs(yn1-yn) >=e)):
        xn = xn1
        yn = yn1
        xn1 = f1(yn)
        yn1 = f2(xn)
        n += 1
    print ('Simple iteration:')
    print ('x=', xn, '\ny=',yn,'\nThe amount of iteration = ',n)
    return xn, yn
simpleIterationMethod(x0, y0, e)

#Check results:
def funcChecker(z):
    return math.sin(z[0] + 1) - z[1] - 1, 2 * z[0] + math.cos(z[1]) - 2
solve_check = optimize.root(funcChecker, [0.,0.], method = 'hybr')

print('Checked Result is: ' + str(solve_check.x))