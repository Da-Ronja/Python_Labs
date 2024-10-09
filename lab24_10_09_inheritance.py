### 1. Veichle Inheritance ###
"""
Create a Python program that models a hierarchy of vehicles using inheritance. Start with a base class
Vehicle, and then create two or more derived classes (e.g., Car, Bicycle, Motorcycle) that inherit from
the Vehicle class. Each class should have specific attributes and methods related to the type of vehicle
it represents.
"""

# 1. Define the Vehicle base class with common attributes such as make, model, and year, and methods like start(), stop(), and fuel_up().
class Vehicle: # Base class Vehicle
    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def __str__(self) -> str:
        return f"Make: {self.make}\n - Model: {self.model}\n - Year: {self.year}\n - Color: {self.color}"

    def start(self):
        print(f"{self.make} {self.model} started.")
    
    def stop(self):
        print(f"{self.make} {self.model} stopped.")
    
    def fuel_up(self):
        print(f"{self.make} {self.model} fueled up.")

# 2. Create derived classes for different types of vehicles, e.g., Car, Bicycle, and Motorcycle. 
## Each derived class should inherit from the Vehicle base class and add attributes and methods specific to that type of vehicle. 
## For example, the Car class might have attributes like num_doors, and the Bicycle class could have attributes like num_gears.

# 3. Implement specific methods for each derived class. For instance, 
# the Car class might have a method to honk the horn, and 
# the Bicycle class could have a method to ring the bell.

class Car(Vehicle): # Derived class Car
    def __init__(self, make, model, year, color, num_doors):
        super().__init__(make, model, year, color)
        self.num_doors = num_doors
    
    def __str__(self) -> str:
        return f"{super().__str__()}\n - Number of Doors: {self.num_doors}"

    def honk_horn(self):
        print(f"{self.make} {self.model} honked the horn.")

class Bicycle(Vehicle): # Derived class Bicycle
    def __init__(self, make, model, year, color, num_gears):
        super().__init__(make, model, year, color)
        self.num_gears = num_gears
    
    # def __str__(self) -> str:
    #     return f"{super().__str__()}\n - Number of Gears: {self.num_gears}"
    
    def ring_bell(self):
        print(f"{self.make} {self.model} rang the bell.")

class Motorcycle(Vehicle): # Derived class Motorcycle
    def __init__(self, make, model, year, color):
        super().__init__(make, model, year, color)

# 4. Create instances of each vehicle type and demonstrate their specific methods and attributes. 
# For example, you can create a car, bicycle, and motorcycle, and call methods like start(), stop(),
# and their specific methods like honk_horn() or ring_bell().

car = Car("Toyota", "Corolla", 2021, "Red", 4)
print(car)
car.start()
car.stop()
car.honk_horn()
car.fuel_up()

bicycle = Bicycle("Monark", "Emma 3-vxl", 2021, "Black", 3)
print(f"{super(Bicycle, bicycle).__str__()}\n - Number of Gears: {bicycle.num_gears}")
bicycle.start()
bicycle.stop()
bicycle.ring_bell()
bicycle.fuel_up()

motorcycle = Motorcycle("Harley-Davidson", "Street 750", 2021, "Black")
print(motorcycle)
motorcycle.start()
motorcycle.stop()
motorcycle.fuel_up()