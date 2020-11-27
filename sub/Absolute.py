# |5| == 5, |-3| == 3
def absolute(number):
    if number > 0:
        return number
    else:
        return number*(-1)


x = float (input("Введіть число:"))
print(f"|{x}| == {absolute(x)}")