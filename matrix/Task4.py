# Циклічно зсунути парні стовпці матриці зліва направо на k позицій
# зсув 1 2 3 4 5  -> 5 1 2 3 4 -> 4 5 1 2 3 -> 3 4 5 1 2
# зсув парних 1* 2 3* 4 5* -> 5 2 1 4 3 -> 3 2 5 4 1
from random import randint
n = int(input("Кількість рядків"))
m = int(input("Кількість стовпців"))
matrix = [[randint(0, 9) for j in range(m)] for i in range(n)]
print(matrix)
k = int(input("На скільки позицій зсунути стовпці "))
for row in matrix:
    moveElements = []
    stayElements = []
    for j in range(m):
        if j % 2 == 0:
            moveElements.append(row[j])
        else:
            stayElements.append(row[j])
    movedRow = moveElements[-k:] + moveElements[:len(moveElements)-k]
    for j in range(m):
        if j % 2 == 0:
            row[j] = movedRow[j//2]
        else:
            row[j] = stayElements[j//2]
print(matrix)