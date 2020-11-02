# x, y є R**3, z = 2x+3y
# x = (1, 2, 3) y=(4,5,6)  z = (2*1+3*4, ..., ... )

# print("x1=")
# x1 = float(input())
# print("x2=")
# x2 = float(input())
# print("x3=")
# x3 = float(input())
# print("y1=")
# y1 = float(input())
# print("y2=")
# y2 = float(input())
# print("y3=")
# y3 = float(input())
# z1 = 2*x1+3*y1
# z2 = 2*x2+3*y2
# z3 = 2*x3+3*y3
# print(f"z=({z1}, {z2}, {z3})")


#max = 0
# (7,5,10) -> (7,5,0)
# print("a")
# a = float(input())
# print("b")
# b = float(input())
# print("c")
# c = float(input())
# if a>b and a>c:
#     a = 0.0
# elif b>a and b>c:
#     b = 0.0
# else:
#     c = 0.0
# print(a,b,c)


#A(x1,y1) B(x2,y2) C(x3,y3) D(x4,y4) - чи прямокутник
# from math import sqrt
# print("x1=")
# x1 = float(input())
# print("y1=")
# y1 = float(input())
# print("x2=")
# x2 = float(input())
# print("y2=")
# y2 = float(input())
# print("x3=")
# x3 = float(input())
# print("y3=")
# y3 = float(input())
# print("x4=")
# x4 = float(input())
# print("y4=")
# y4 = float(input())
# AB = sqrt((x2-x1)**2+(y2-y1)**2)
# AC = sqrt((x3-x1)**2+(y3-y1)**2)
# AD = sqrt((x4-x1)**2+(y4-y1)**2)
# BC = sqrt((x3-x2)**2+(y3-y2)**2)
# BD = sqrt((x4-x2)**2+(y4-y2)**2)
# CD = sqrt((x4-x3)**2+(y4-y3)**2)
# eps = 0.0001
# if abs(AB**2+BC**2-AC**2)<eps and abs(AD**2+AB**2-BD**2)<eps and abs(BC**2+CD**2-BD**2)<eps and abs(CD**2+AD**2-AC**2)<eps:
#     print("ABCD - прямокутник")
# else:
#     print("ABCD - не прямокутник")


# 1, if 2x**2-3=0
#2*x, if 2x**2-3>0
#x, if 2x**2-3<0
# print("x=")
# eps = 0.0000001
# x = float(input())
# if abs(2*x**2-3) < eps:
#     res = 1
# elif 2*x**2-3>0:
#     res = 2*x
# else:
#     res = x
# print(res)


# чи належить x {1,2,3} U [-7,0)
print("x=")
x = float(input())
if (x == 1 or x == 2 or x ==3) or (x >= -7 and x < 0):
    print("х належить  {1,2,3} U [-7,0)")
else:
    print("х не належить  {1,2,3} U [-7,0)")