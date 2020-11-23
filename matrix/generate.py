vector = [1, 2, 3]
# літерал
# matrix = [[1, 2, 3],
#           [4, 5, 6],
#           [7, 8, 9],
#           [1, 1, 1]]

# цикли
# n = int(input("Кількість рядків ="))
# m = int(input("Кількість стовпців ="))
# matrix2 = []
# for i in range(n):
#     matrix2.append([])
#     for j in range(m):
#         aij = int(input(f"a[{i+1},{j+1}]="))
#         matrix2[i].append(aij)
# print(matrix2)

#ще цикли
# n = int(input("Кількість рядків ="))
# m = int(input("Кількість стовпців ="))
# matrix3 = []
# print(f"введіть матрицю {n} на {m}")
# for i in range(n):
#     row = list(map(int, input().split()))
#     matrix3.append(row)
# print(matrix3)

# генераторів
from random import randint
n = int(input("Кількість рядків ="))
m = int(input("Кількість стовпців ="))
randomMatrix = [[randint(-100, 100) for j in range(m)] for i in range(n)]
print(randomMatrix)