# Дано матрицю A. Перевірити, чи є дана матриця нижньою трикутною матрицею.
# 1 0 0
# 2 1 0
# 2 3 1

n = int(input("Кількість рядків ="))
m = int(input("Кількість стовпців ="))
matrix = []
print(f"введіть матрицю {n} на {m}")
for i in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

isLowTriangle = True
for i in range(n):
    for j in range(i+1, n):
        if not matrix[i][j] == 0:
            isLowTriangle = False
            break
if isLowTriangle:
    print("Матриця є нижньою трикутною")
else:
    print("Матриця не є нижньою трикутною")
