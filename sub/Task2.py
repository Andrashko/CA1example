#Дано послідовність натуральних чиcел  .
# Використовуючи підпрограму знаходження найбільшої та найменшої цифри, знайти число, у
# яке містить найбільшу цифру та число, яке містить найменшу цифру.
from random import randint


def maxDigit(number):
    res = 0
    while number > 0:
        lastDigit = number % 10
        if lastDigit > res:
            res = lastDigit
        number = number // 10
    return res


def minDigit(number):
    res = 9
    while number > 0:
        lastDigit = number % 10
        if lastDigit < res:
            res = lastDigit
        number = number // 10
    return res


n = int(input("кількість чисел="))
seq = [randint(1, 10000) for i in range(n)]
print(seq)
numberWithMaxDigit = seq[0]
numberWithMinDigit = seq[0]
for number in seq:
    if maxDigit(number) > maxDigit(numberWithMaxDigit):
        numberWithMaxDigit = number
    if minDigit(number) < minDigit(numberWithMinDigit):
        numberWithMinDigit = number
print(f" число з макс цифрою {numberWithMaxDigit} та число з мін цифрою {numberWithMinDigit}")