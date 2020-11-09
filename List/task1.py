# Дано одновимірний масив дійсних чисел. Знайти суму елементів, які розташовані до першого від’ємного елемента.
n = int(input("Введіть кількість елементів:"))
numbers = list(map(float, input(f"Введіть список з {n} дійсних чисел через кому:").split(",")))

firstNegative = 0
s = 0
for element in numbers:
    if element < 0:
        firstNegative = element
        break
    s += element

if firstNegative == 0:
    print("Відємний елемент відсутній")
else:
    print(f"Сума елементів до першого відємного рівна {s}")