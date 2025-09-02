class Car:
    total_cars = 0

    def __init__(self, make, model):
        self.make = make
        self.model = model
        Car.total_cars += 1

    def display_car(self):
        return f"{self.make} {self.model}"

    @staticmethod
    def get_total_cars():
        return Car.total_cars


car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")
car3 = Car("Ford", "Mustang")

print(car1.display_car())
print(car2.display_car())

print("Total cars created:", Car.get_total_cars())  # 3
