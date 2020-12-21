#Розробити клас що виконує основні функції бази даних а також містить методи для зберігання данних у файлах та зчитування із файлу
#3. Телефонний довідник кафедри. База даних телефонних номерів співробітників:
#прізвище, ім’я, по батькові, посада, номер стаціонарного телефону, номер мобільного телефону. Організувати вибір за довільним запитом.
from datetime import datetime

class Employee:
    def __init__(self, surname, name, second_name, post, home_phone, mobile_phone):
        self.surname = surname
        self.name = name
        self.second_name = second_name
        self.post = post
        self.home_phone = home_phone
        self.mobile_phone = mobile_phone
        self.__age = 0
        self.created = datetime.now()
        self.chaged = datetime.now()

    @property
    def full_name(self):
        return f"{self.surname} {self.name} {self.second_name}"

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        self.chaged = datetime.now()
        if value > 0:
            self.__age = value
        else:
            raise Exception("Відємний вік")

    def __str__(self):
        return f"{self.post} {self.surname} {self.name} {self.second_name} <{self.mobile_phone}, {self.home_phone}>"

    def __repr__(self):
        return str(self)


class Cathedra:
    def __init__(self, file_name):
        self.__list = []
        self.file_name = file_name

    def __repr__(self):
        return self.__list

    def __str__(self):
        return str(self.__list)

    @property
    def count(self):
        return len(self.__list)

    def add(self, employee):
        self.__list.append(employee)

    def save_to_file(self):
        with open(self.file_name, "w") as file:
            for employee in self.__list:
                file.write(f"{employee.surname};{employee.name};{employee.second_name};{employee.post};{employee.home_phone};{employee.mobile_phone}\n")

    def load_from_file(self):
        self.__list.clear()
        with open(self.file_name, "r") as file:
            for row in file:
                surname, name, second_name, post, home_phone, mobile_phone = row.split(";")
                mobile_phone = mobile_phone[:-1]
                home_phone = int(home_phone)
                self.__list.append(Employee(surname, name, second_name, post, home_phone, mobile_phone))

    def find_by_surname(self, surname):
        for employee in self.__list:
            if employee.surname == surname:
                return employee
        return None

SATO = Cathedra("sato.txt")
# SATO.add(Employee("Андрашко", "Юрій", "Васильович", "доцент", "0311234567", "0509429407"))
# SATO.add(Employee("Брила", "Андрій", "Юрійович", "доцент", "031234567", "050913556"))
SATO.load_from_file()
print(SATO)
print(SATO.find_by_surname("Андрашко"))
print(SATO.find_by_surname("Мич"))
# a = Employee("Андрашко", "Юрій", "Васильович", "доцент", "0311234567", "0509429407")
#
# print(a.age)
# print(a.full_name)
# n = input()
# a.age = 31
# print(a.created, a.chaged)