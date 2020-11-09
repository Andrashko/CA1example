# літерал
a = [1, 2, 3]
print(a)

# конструктор
b = list((1, 2, 3))
print(b)

# генератор
c = [x for x in range(1, 4)]
print(c)

#цикл
d = list()
for x in range(1, 4):
    d.append(x)
print(d)

#множення
e = [0]*3
for x in range(3):
    e[x] = x+1
print(e)
