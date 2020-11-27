#створити підпрограму для розвязування квадратного рівняння

def solveSquareEquation(a, b, c):

    def discriminant(a, b, c):
        return b**2-4*a*c

    if discriminant(a, b, c) < 0:
        return []
    else:
        x1 = (-b + discriminant(a, b, c) ** (0.5) ) / (2 * a)
        x2 = (-b - discriminant(a, b, c) ** (0.5) ) / (2 * a)
        return [x1, x2]


a = 1
b = 5
c = 6
print(f"{a}x**2+{b}x+{c}=0 має розв'язки {solveSquareEquation(a,b,c)}")
