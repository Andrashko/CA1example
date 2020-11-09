#Знайти вектор c=2(a+b)-3(a-b), де a,b,c є Rn.
n = int(input("n="))
a = list(map(float, input("Введіть координати вектора а через пробіл:").split()))
b = list(map(float, input("Введіть координати вектора b через пробіл:").split()))
c = [2*(a[i]+b[i])-3*(a[i]-b[i]) for i in range(n)]
print("c=", c)