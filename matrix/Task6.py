#Дана цілочислова квадратна матриця. Визначити кількість рядків, у яких елементи упорядковані за зростанням

from random import randint
n = int(input("Кількість рядків і стовпців"))
matrix = [[randint(0, 9) for j in range(n)] for i in range(n)]
print(matrix)

count = 0
for row in matrix:
    isIncrease = True
    for j in range(1, n):
        if row[j-1] >= row[j]:
            isIncrease = False
            break
    if isIncrease:
        count += 1
print(f"Кількість зростаючих рядків = {count}")
