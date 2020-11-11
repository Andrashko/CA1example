# Перетворити масив таким чином, щоб спочатку розміщувались всі елементи,
# ціла частина яких лежить в інтервалі [a,b], а потім всі інші.
from random import random
n = int(input("n="))
randomArray = [random() * 200 - 100 for _ in range(n)]
print(randomArray)

a = int(input("a="))
b = int(input("b="))
# conditionArr = []
# for el in randomArray:
#     if a <= int(el) <=b:
#         conditionArr.append(el)
# print(conditionArr)
# notConditionArr = []
# for el in randomArray:
#     if not el in conditionArr:
#         notConditionArr.append(el)
# print(notConditionArr)
# randomArray = conditionArr + notConditionArr
# print(randomArray)
conditionArr = [el for el in randomArray if a <= int(el) <=b]
notConditionArr = [el for el in randomArray if el not in conditionArr]
print(conditionArr+notConditionArr)