# Побудувати масив V=(vi), елементи якого задаються формулою:
# де a, b, х – вводяться з клавіатури. Обчислити добуток елементів масиву V з парними індексами

a = float(input("a="))
b = float(input("b="))
x = float(input("x="))
n = int(input("Кількість елементів V:"))

V = [a, b]
for i in range(2, n):
    V.append((1/2)*(V[i-1]+x/V[i-2]))
print(V)
d = 1
for i in range(0, n, 2):
    d *= V[i]
print("Добуток ", d)
