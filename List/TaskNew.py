# вилучити з масива всі елементи менші за третій
from random import random
n = int(input("n="))
randomArray = [random() * 200 - 100 for _ in range(n)]
print(randomArray)
newArr = [el for el in randomArray if el >= randomArray[2]]
print(newArr)