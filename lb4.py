import numpy as np
import math

#Matrix AB-BA
A = np.matrix('1, 2; 4, -1')
print(A)
B = np.matrix('2, -3; -4, 1')
print(B)

C = A.dot(B)
D = B.dot(A)
F = C - D
print('Matrix AB - BA result:')
print(F)

#Stepen Matrix
C = np.matrix('-1, 2; 0, 1')
D = np.linalg.matrix_power(C, 2)
print("Matrix Power result: ")
print(D)

#Dobutok Matrix
A = np.matrix('5, 8, -4; 6, 9, -5; 4, 7, -3')
B = np.matrix('3, 2, 5; 4, -1, 3; 9, 6, 5')
C = A.dot(B)
print('Matrix A*B result:')
print(C)

#Vyznachnyky -1
A = np.matrix('2, 4, 5; 1, 1, 2; 2, 4, 3')
det_A = round(np.linalg.det(A))
print("Matrix Determinator 01:")
print(det_A)

#Vyznachnyky -2
A = np.matrix('2, 3, 4, 1; 1, 2, 3, 4; 3, 4, 1, 2; 4, 1, 2, 3')
det_A = round(np.linalg.det(A))
print("Matrix Determinator 02:")
print(det_A)

#Mirrored Matrix
A = np.matrix('1, 1, 1, 1; 1, 1, -1, -1; 1, -1, 1, -1; 1, -1, -1, 1')
A_inv = np.linalg.inv(A)
print(A)
print("Inversed Matrix:")
print(A_inv)

#Matrix Rank
A = np.matrix('1, 2, 3, 4; 3, -1, 2, 5; 1, 2, 3, 4; 1, 3, 4, 5')
rank = np.linalg.matrix_rank(A)
print('Matrix Rank:')
print(A)
print(rank)

#Kramer Method + Matrix Method

print('Kramer Method:')
A = np.matrix('14, 4, 6; 5, -3, 2; 10, -11, 5')
print(A)
B = np.matrix('30; 15; 36')
print(B)
A_det = np.linalg.det(A)
print(A_det)
X_m = np.matrix(A)
X_m[:, 0] = B
print(X_m)

Y_m = np.matrix(A)
Y_m[:, 1] = B
print(Y_m)

Z_m = np.matrix(A)
Z_m[:, 2] = B
print(Z_m)

x = np.linalg.det(X_m) / A_det
y = np.linalg.det(Y_m) / A_det
z = np.linalg.det(Z_m) / A_det
print('Result: ', x, y, z)

#Matrix Method
print('Matrix Method below:')

A = np.matrix('14, 4, 6; 5, -3, 2; 10, -11, 5')
print(A)
B = np.matrix('30; 15; 36')
print(B)

A_inv = np.linalg.inv(A)
print(A_inv)

X = A_inv.dot(B)
print('Result: ')
print(X)

Y = np.linalg.solve(A, B)
print('np.linalg.solve Check...')
print(Y)

#Selected Task #6
print('Creation of random 3/3 matrix...')
A = np.random.randint(-15, 15, size=(3, 3))
print(A)

print('Find mean value in all rows: ')
print(A.mean(0))

print('Lowest through all mean values: ')
print(min(A.mean(0)))