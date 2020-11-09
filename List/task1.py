# Дано одновимірний масив дійсних чисел. Знайти суму елементів, які розташовані до першого від’ємного елемента.
n = int(input("Введіть кількість елементів:"))
numbers = list(map(float, input(f"Введіть список з {n} дійсних чисел через кому:").split(",")))

firstNegative = 0
for element in numbers:
    if element < 0:
        firstNegative = element
        break

if firstNegative == 0:
    print("Відємних елементів в масиві нема")
else:
    s = 0
    for element in numbers:
        if element == firstNegative:
            break
        s += element
    print(f"Сума елементів до першого відємного рівна {s}")