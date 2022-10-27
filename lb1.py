import math
from scipy.misc import derivative

a = -2.
b = 2.
eps = 0.001

def f(x):
    return 3*pow(x, 4) - 4*pow(x, 3) + pow(x, 2) - 2*x - 3

def hordeMethod(a, b, eps):
    if(abs(f(b) - f(a)) < eps):
        return
    if(f(a) * derivative(f, a, n = 2)):
        x1 = a
        x2 = b
    else:
        x1 = b
        x2 = a
    xR1 = x2 - (x2 - x1) * f(x2) / (f(x2) - f(x1))
    while (abs(f(xR1) - f(x2)) > eps):
        x2 = xR1
        xR1 = x2 - (x2 - x1) * f(x2) / (f(x2) - f(x1))
        print (xR1)
    else:
        print("x = ", xR1)

hordeMethod(a, b, eps)