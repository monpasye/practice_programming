import numpy as np
my_array = np.arange(10, 70, 2)
print("Полученный массив:")
print(my_array)

A = my_array.reshape(6,5)
A = A.transpose()
print("Транспонированная матрица А:")
print(A)

A = A * 2.5 - 5
print("Матрица А после арифметических действий:")
print(A)

B = np.random.uniform(0, 10, (6, 3))
print("Полученная матрица В:")
print(B)

a = A.sum(axis=1)
b = B.sum(axis=0)
print("Полученный вектор а:", a)
print("Полученный вектор b:", b)

C = np.dot(A, B)
print("Произведение А на В: ")
print(C)

A = np.delete(A, 2, 1)
B_added = np.random.uniform (10, 20, (6, 3))
B = np.hstack ((B, B_added))
print("А с удаленным третьим столбцом: ")
print(A)
print("В с добавленными столбцами: ")
print(B)

A_det = np.linalg.det(A)
B_det = np.linalg.det(A)
if abs(A_det) > 1e-10:
    A_inv = np.linalg.inv(A)
    print("Обратная матрица А:")
    print(A_inv)
else:
    print("Определитель матрицы А равен нулю, а значит найти обратную матрицу невозможно")
if abs(B_det) > 1e-10:
    B_inv = np.linalg.inv(B)
    print("Обратная матрица В:")
    print(B_inv)
else:
    print("Определитель матрицы В равен нулю, а значит найти обратную матрицу невозможно")

print("Возведенная в шестую степень А:")
print(np.linalg.matrix_power(A, 6))
print("Возведенная в четырнадцатую степень В:")
print(np.linalg.matrix_power(B, 14))

A = np.array([
    [4, -3.4, 1, 1.8],
    [-2, 8, 0, -9],
    [2, -2.5, -7, 4],
    [1, -1, 5, 1]
])
b = np.array([6, -4.8, 10, 3])
x = np.linalg.solve(A, b)
print("Решение первого варианта: ")
print(x)