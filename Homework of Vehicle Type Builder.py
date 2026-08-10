# Vehicle Type Builder

class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def move(self):
        print("The vehicle is moving.")


class Car(Vehicle):
    def move(self):
        print(self.brand, "car is driving.")


car = Car("Toyota")

car.move()

print("Is Car a subclass of Vehicle?", issubclass(Car, Vehicle))

# Using super()
class SportsCar(Car):
    def __init__(self, brand):
        super().__init__(brand)

sports_car = SportsCar("BMW")
sports_car.move()