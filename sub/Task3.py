# Нехай  . Визначити
from math import cos


def x(i):
    if i == 0:
        return 2
    elif i == 1:
        return 1
    else:
        return (cos(x(i-1)))**x(i-2)


n = int(input("n="))
print(f"x{n}={x(n)}")

