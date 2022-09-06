class Vahicle:

    def __init__(self,
                 producer: str,
                 model: str,
                 year: int,
                 tank_capacity: float,
                 maxspeed: int,
                 fuel_consumption: float,
                 tank_level: float = 0,
                 odometer_value: int = 0
                 ):
        self.producer = producer
        self.model = model
        self.year = year
        self.tank_capacity = tank_capacity
        self.maxspeed = maxspeed
        self.fuel_consumption = fuel_consumption
        self.tank_level = tank_level
        self.odometer_value = odometer_value

    def __repr__(self):
        return f'Vahicle info: model - {self.model}, year - {self.year}, odometer value - {self.odometer_value}, ' \
               f'max speed - {self.maxspeed}, fuel consumption - {self.fuel_consumption}, tank level - {self.tank_level}'

    def refueling(self):
        diff = self.tank_capacity - self.tank_level
        self.tank_level = self.tank_capacity
        print(f"The vahicle is filled with {diff} liters of fuel")

    def __race(self, distance: float):
        used_fuel = (self.fuel_consumption * distance) / 100
        time_taken = distance / (self.maxspeed * 0.8)
        self.tank_level -= used_fuel
        self.odometer_value += distance
        return {
            'distance traveled': distance,
            'time taken in min': time_taken * 60,
            'tank level': self.tank_level
        }

    def race(self, distance: float):
        if (self.tank_level*100)/self.fuel_consumption <= distance:
            distance = (self.tank_level*100)/self.fuel_consumption
        return self.__race(distance)

    def lend_fuel(self, other):
        if self.tank_level == self.tank_capacity or other.tank_level == 0:
            print('Нічого страшного, якось розберуся')
        else:
            diff = self.tank_capacity - self.tank_level
            if diff > other.tank_level:
                diff = other.tank_level
            self.tank_level += diff
            other.tank_level -= diff
            print(f'Дякую, бро, виручив. Ти залив мені {diff} літрів пального')

    def __eq__(self, other):
        return self.year == other.year and self.odometer_value == other.odometer_value


car1 = Vahicle(producer='AUDI', model='q7', year=2022, tank_capacity=100, maxspeed=250, fuel_consumption=14)
car1.refueling()
print(car1.race(89))
print(car1)

car2 = Vahicle(producer='AUDI', model='q6', year=2022, tank_capacity=100, maxspeed=220, fuel_consumption=10.5)
car2.refueling()
print(car2.race(89))
print(car1 == car2)

print(car1.race(108))
print(car1.race(520))

car1.lend_fuel(car2)
print(car1.race(30))
print(car1.race(50))
print(car1.race(70))


print(car1 == car2)

car2.refueling()
car1.lend_fuel(car2)
