from pickletools import optimize
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange #імпортуємо функцію lagrange з бібліотки

x=np.array([-3.,-1.,0.5,2.5], dtype=float)
y=np.array([-8.,10.,-8.,20.], dtype=float)

def definable_func(b):
    return pow(b,3) + 2 * pow(b,2) - 7 * b - 4

def lagranz_custom(x,y,t):
    z=0
    for j in range(len(y)):
        p1=1; p2=1
        for i in range(len(x)):
            if i==j:
                p1=p1*1; p2=p2*1   
            else: 
                p1=p1*(t-x[i])
                p2=p2*(x[j]-x[i])
        z=z+y[j]*p1/p2
    return z

xnew=np.linspace(np.min(x),np.max(x),100) #точки, за якими будуємо графік
ynew=[lagranz_custom(x,y,i) for i in xnew]

plt.plot(x,y,'o',xnew,ynew) #будуємо графік функції Лагранжа
plt.title('Lagrange Polynomial_1')

plt.grid(True)
plt.show()

#Check function results:
#x = -3
print(definable_func(-3))
#x = -1
print(definable_func(-1))
#x = 0,5
print(definable_func(0.5))
#x = 2,5
print(definable_func(2.5))


f = lagrange(x, y)
fig = plt.figure(figsize = (10,8))
plt.plot(xnew, f(xnew), 'b', x, y, 'ro')
plt.title('Lagrange Polynomial_2')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()