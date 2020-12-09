# Об’єкт “Черга” (реалізація черги за допомогою одновимірного масиву цілих чисел)
# поля
# 	для зберігання номерів першого та останнього елементів черги;
# 	масив елементів;
# методи
# 	виведення на екран;
# 	додавання нового елементу;
# 	видалення елементу;
# 	знаходження суми елементів.
# pus (4) [1, 2, 3] -> [1, 2, 3, 4]
# pop() [1, 2, 3, 4] -> [2, 3, 4]

class Queue:
    """Queue"""
    first = 0
    last = 0
    maxNum = 2

    def __init__(self):
        self.array = [0] * self.maxNum

    def printToScreen(self):
        print(f"Queue \n array: {self.array}, \n first :{self.first},\n last: {self.last}")

    def push(self, element):
        if self.last < self.maxNum:
            self.array[self.last] = element
            self.last += 1
        else:
            print("переповнення черги")

    def pop(self):
        self.first += 1
        return self.array[self.first-1]

    def sumElements(self):
        return sum(self.array[self.first:self.last])


q = Queue()
q.push(1)
q.push(2)
q.push(3)
print(q.sumElements())
print(q.pop())
print(q.sumElements())
q.printToScreen()
