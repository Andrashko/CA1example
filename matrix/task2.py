# Побудувати квадратну матрицю А, елементи якої задаються формулою:
from math import factorial
n = int(input("Кількість рядків і стовпців ="))
matrix = []
for i in range(n):
    matrix.append([])
    for j in range(n):
        if (i+j) % 2 == 0:
            element = factorial(i)
        else:
            element = 0
            dod = 1
            for k in range (j+1):
                element += dod ** 2
                dod += k+2
        matrix[i].append(element)
print(matrix)
# Сформувати одновимірний масив b, i-ий елемент якого є добутком усіх елементів i-го стовпчика матриці А.
b = []
for j in range(n):
    dob = 1
    for i in range(n):
        dob *= matrix[i][j]
    b.append(dob)
print(b)