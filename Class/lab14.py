# Створити клас TVSeries, який представляє прогресію і містить методи для
# знаходження n -го члена прогресії і знаходження суми перших n членів цієї
# прогресі. На основі цього класу створити класи нащадки, які представляють
# арифметичні та геометричні прогресії. Випадковим чином згенерувати дані для n
# прогресій (геометрична, арифметична, геометрична, арифметична, і т.д.). Знайти
# суму перших m членів прогресії, n -товий член якої є найбільшим

class TVSeries:
    def __init__(self, elem):
        self.elem = elem

    def elemN(self, n):
        return self.elem

    def sumN(self, n):
        s = 0
        for i in range(n):
            s += self.elemN(i)
        return s

    def __str__(self):
        return f"{self.elemN(0)}, {self.elemN(1)}, {self.elemN(2)}, ..."


class ArithmeticSeries (TVSeries):
    def __init__(self, a0, d):
        self.a0 = a0
        self.d = d

    def elemN(self, n):
        return self.a0 + n * self.d


class GeometricSeries(TVSeries):
    def __init__(self, b0, q):
        self.b0 = b0
        self.q = q

    def elemN(self, n):
        return self.b0 * self.q ** n


from random import randint

n = int(input("n="))
series = []
for i in range(n//2):
    series.append(ArithmeticSeries(randint(0, 10), randint(0, 10)))
    series.append(GeometricSeries(randint(0, 10), randint(0, 10)))
print([str(s) for s in series])

seriesWithMaxElementN = series[0]

for s in series:
    if s.elemN(n) > seriesWithMaxElementN.elemN(n):
        seriesWithMaxElementN = s

print(seriesWithMaxElementN)
m = int(input("m="))
print(f"сума перших {m} елеметнів = {seriesWithMaxElementN.sumN(m)}")

