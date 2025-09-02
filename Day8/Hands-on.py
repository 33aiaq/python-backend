class Vehicle:
    def __init__(self, brand, model, speed=0):
        self.brand = brand
        self.model = model
        self.speed = speed

    def start(self):
        print(f"{self.brand} {self.model} is starting.")

    def stop(self):
        print(f"{self.brand} {self.model} is stopping.")

    def drive(self):
        print(f"{self.brand} {self.model} is driving at {self.speed} km/h.")

    def __repr__(self):
        return f"Vehicle({self.brand}, {self.model})"


class Car(Vehicle):
    def __init__(self, brand, model, speed=0, doors=4):
        super().__init__(brand, model, speed)
        self.doors = doors

    def drive(self):
        print(f"Car {self.brand} {self.model} is cruising at {self.speed} km/h.")

    def open_trunk(self):
        print(f"Trunk of {self.brand} {self.model} is open.")

    def __repr__(self):
        return f"Car({self.brand}, {self.model}, doors={self.doors})"


class Supercar(Vehicle):
    def __init__(self, brand, model, speed=0, doors=2):
        super().__init__(brand, model, speed)
        self.doors = doors

    def drive(self):
        print(f"Bicycle {self.brand} {self.model} is pedaling at {self.speed} km/h.")

    def ring_bell(self):
        print(f"{self.brand} {self.model} bell rings: Ding Ding!")

    def __repr__(self):
        return f"Bicycle({self.brand}, {self.model}, gears={self.doors})"


vehicles = [
    Car("Toyota", "Camry", 80, doors=4),
    Supercar("Cadillac", "ATS", 120, doors=2),
    Vehicle("Honda", "bike2", 50)
]

for v in vehicles:
    v.drive()

vehicles[0].open_trunk()
vehicles[1].ring_bell()
