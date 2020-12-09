#  Об’єкт “Готель” (використати члени-класи)
# поля
# ▪ назва готелю;
# ▪ тип готелю;
# ▪ кількість послуг та інформація про послуги як масив (для кожної послуги зберігається: назва послуги, вартість, тривалість);
# ▪ кількість та масив інформації про кімнати (порядковий номер,
#           кількість місць, вартість кімнати на одну добу, дата заїзду та дата виїзду жильців);
# методи
# ▪ виведення на екран послуг, які можуть бути виконані за вказану суму грошей та вказаний термін часу;
# ▪ виведення на екран вільних номерів з вказаною кількістю місць;
# ▪ визначення суми грошей, яку повинні заплати жильці вказаної кімнати при від’їзді;
# ▪ визначення  кількості вільних місць за умови, що нових жильців  приймати не будуть.
from datetime import date, datetime


class Service:
    def __init__(self, name, price, duration):
        self.name = name
        self.price = price
        self.duration = duration

    def __str__(self):
        return f"Service name :{self.name}, price :{self.price}, dduration: {self.duration}"


class Room:
    def __init__(self, no, count, price, inDate, outDate):
        self.no = no
        self.count = count
        self.price = price
        self.inDate = inDate
        self.outDate = outDate

    def __str__(self):
        return f"Room {self.no}"

    def isBusy(self):
        return self.inDate <= datetime.now().date() <= self.outDate

    def calcSumToPay(self):
        days = (self.outDate - self.inDate).days
        return days * self.price


class Hotel:
    def __init__(self, name, type, services, rooms):
        self.name = name
        self.type = type
        self.services = services
        self.rooms = rooms

    def __str__(self):
        return f"Hotel {self.name}"

    def seviceCount(self):
        return len(self.services)

    def roomCount(self):
        return  len(self.rooms)

    def printServices(self, money, time):
        okServices = [str(service) for service in self.services if service.price <= money and  service.duration <= time]
        print(okServices)

    def printFreeRooms(self):
        print("Free Rooms")
        for room in self.rooms:
            if not room.isBusy():
                print(room)

    def calcToPayForRoom(self, roomNo):
        for room in self.rooms:
            if room.no == roomNo:
                return room.calcSumToPay()
        print("Такої кімнати нема")

    def calcFreeRooms(self):
        count = 0
        for room in self.rooms:
            if not room.isBusy():
                count += room.count
        return count

vizyt = Hotel("Візит", "***", [Service("Спа", 1000, 2), Service("Музика", 250, 1), Service("Басейн", 100, 0.5), Service("Зал", 150, 3)],
              [Room(303, 2, 499, date(2020, 12, 9), date(2020, 12, 19)),
               Room(107, 1, 350, date(2020, 11, 30), date(2020, 12, 2)),
               Room(404, 1, 350, date(2020, 12, 30), date(2021, 1, 8))
               ])


print(vizyt.calcToPayForRoom(404))