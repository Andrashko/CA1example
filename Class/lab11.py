# Клас “комплексне число” – TComplex
# поля
# ▪ для зберігання дійсної і уявної частин;
# методи
# ▪ конструктор без параметрів, конструктор з параметрами,
# конструктор копіювання;
# ▪ введення/виведення даних;
# ▪ перевантаження операторів +, –, *, /

class TComplex:

    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

    def copy(self):
        return TComplex(self.re, self.im)

    def __str__(self):
        return f"{self.re}+{self.im}i"

    def input(self):
        print("Введіть комплексне число")
        self.re = float(input("Re="))
        self.im = float(input("Im="))

    def __add__(self, other):
        return TComplex(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        return TComplex(self.re - other.re, self.im - other.im)

    def __mul__(self, other):
        return TComplex(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)

    def __truediv__(self, other):
        return TComplex()

    def __eq__(self, other):
        return self.re == other.re and self.im == other.im

   

complexNumber = TComplex(1, 2)
noParametrComplexNumber = TComplex()
copyNumber = complexNumber.copy()
complexNumber.re = 3
# noParametrComplexNumber.input()
print(f"{copyNumber} + {complexNumber} = { complexNumber + copyNumber} ")
print(f" {complexNumber} -{copyNumber}  = { complexNumber - copyNumber} ")
print(f" {complexNumber} * {copyNumber}  = { complexNumber * copyNumber} ")

if copyNumber == complexNumber:
    print("Yes")
else:
    print("No")