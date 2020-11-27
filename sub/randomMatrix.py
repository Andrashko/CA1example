#підпрограму що генерує випадкову матрицю
from random import randint


def randomMatrix(rowCount, colCount, minVal=-100, maxVal=100):
    res = []
    for i in range(rowCount):
        res.append([])
        for j in range(colCount):
            res[i].append(randint(minVal, maxVal))
    return res


print(randomMatrix(3, 4))