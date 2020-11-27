from math import log, sin, cos, exp


def f(x, y, z):
    if x+y-z > 10:
        return log(x+y-z, 10)
    elif z-10 < x+y < z+1:
        return (abs(x+y)+1)**2
    elif x+y-z == 1:
        return x**2+y**2-z**3
    else:
        return (cos(x))**2+sin(y)-exp(2*z+1)


a = float(input("a="))
b = float(input("b="))
c = float(input("c="))
value = f(2, a, 4) - 5 * f(a, b, -c)
print(f"f(2, a, 4)-5*f(a, b, -c) = {value}")