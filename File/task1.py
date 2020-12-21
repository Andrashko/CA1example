#  Дано текстовий файл, який містить кількість цілих чисел кратну 3. Визначити суму  елементів з номерами, які кратні 3
# file = open("data.txt", "r")
# n = int(file.readline())
# numbers = list(map(int, file.readline().split()))
# file.close()
# print(n)
# print(numbers)
file = open("data2.txt", "r")
numbers = []
for row in file.readlines():
    numbers.append(int(row))
n = len(numbers)
file.close()

s = 0
for i in range(2, n, 3):
    s += numbers[i]
print(f"s={s}")
