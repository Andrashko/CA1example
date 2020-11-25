# Ущільнити задану матрицю, вилучаючи із неї рядки і стовпці, з максимальним елементом.
# 1 2 3
# 5 7 2
# 9 3 1

#2 3
#7 2

# 1 2 3
# 7 9 8
# 2 6 4
# 3 9 2

#1 3
#2 4

from random import randint
n = int(input("Кількість рядків"))
m = int (input("Кількість стовпців"))
matrix = [[randint(0, 9) for j in range(m)] for i in range(n)]
print(matrix)

maxElement = matrix[0][0]
for row in matrix:
    for element in row:
        if element > maxElement:
            maxElement = element
print(f"max = {maxElement}")

DeleteColumn = [False]*m
DeleteRow = [False]*n
for i in range(n):
    for j in range(m):
        if matrix[i][j] == maxElement:
            DeleteColumn[j] = True
            DeleteRow[i] = True
compactMatrix = [[matrix[i][j] for j in range(m) if not DeleteColumn[j]] for i in range(n) if not DeleteRow[i]]
print(compactMatrix)
