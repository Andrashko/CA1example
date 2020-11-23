# Визначити суму від’ємних елементів матриці на побічній діагоналі.
# 1 2 3
# 4 5 6
# 7 8 9
# умова побічної діагонал i + j = n - 1
# умова головної діагонал i = j
#  умова вище i < j


from random import randint
n = int(input("Кількість рядків і стовпців ="))
randomMatrix = [[randint(-100, 100) for j in range(n)] for i in range(n)]
print(randomMatrix)
diagNegative = []
for i in range(n):
    j = n - 1 - i
    if randomMatrix[i][j] < 0:
        diagNegative.append(randomMatrix[i][j])
print(diagNegative)
if len(diagNegative) > 0:
    s = sum(diagNegative)
    print(f"Сума від'ємних елементів побічної діагоналі = {s}")
else:
    print("Нема від'ємних елементів побічної діагоналі")
