numbers = []
with open("data2.txt", "r") as f:
    for row in f:
        numbers.append(int(row))
n = len(numbers)

print(numbers)
