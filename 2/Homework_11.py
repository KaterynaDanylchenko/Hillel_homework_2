# Створіть клас "Транспортний засіб" та підкласи "Автомобіль", "Літак", "Корабель", наслідувані від "Транспортний засіб".
# Наповніть класи атрибутами на свій розсуд. Створіть обʼєкти класів "Автомобіль", "Літак", "Корабель".
class Vehicle:
    name = 'Subaru'
    model = 'Forester'
    lifetime = 10
    weight = 15
    power = '150 horsepower'
    capacity = '4 persons'


class Automobile(Vehicle):
    width = 5.5
    high = 1.5


class Jet(Vehicle):
    passing = '3518 km'
    wingspan = '64.4 м'
    speed = '917 km/hour'


class Boat(Vehicle):
    Draft = '10 m'


print(Vehicle.name)
