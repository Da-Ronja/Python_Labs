from abc import abstractmethod
### 2 Polymorphism ###
"""
Create a Python program that explores polymorphism using a hierarchy of shapes. Start with a base
class Shape, and then create two or more derived classes (e.g., Circle, Rectangle, Triangle) that
inherit from the Shape class. Each shape class should have its own implementation of methods like
area() and perimeter(). These methods will calculate the area and perimeter of the respective shapes.
"""

# 1. Define the Shape base class with methods like area() and perimeter(). 
# You can initialize any common attributes in the base class.
class Shape:
    def __init__(self, name):
        self.name = name
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

# 2. Create derived classes for different shapes, e.g., Circle, Rectangle, and Triangle. 
# Each derived class should inherit from the Shape base class and implement its own version of the area() and perimeter() methods.

# 3. Implement specific methods for each derived class. 
# For example, the Circle class might have a method to calculate its area based on the radius, 
# and the Rectangle class could have a method to calculate its area based on length and width.
class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
    
    def area(self):
        return round(3.14 * self.radius ** 2, 2)
    
    def perimeter(self):
        return round(2 * 3.14 * self.radius, 2)

class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
class Triangle(Shape):
    def __init__(self, name, side1, side2, side3):
        super().__init__(name)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    
    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        return (s * (s - self.side1) * (s - self.side2) * (s - self.side3)) ** 0.5
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3


# Create instances of each shape type and demonstrate the use of polymorphism by calling the area() and perimeter() methods on them.
circle = Circle("Circle", 5)
print("Circle_area:", circle.area(), "\nCircle_perimeter:", circle.perimeter())

rectangle = Rectangle("Rectangle", 4, 6)
print("Rectangle_area:", rectangle.area(), "\nRectangle_perimeter:", rectangle.perimeter())

triangle = Triangle("Triangle", 3, 4, 5)
print("triangle_area:", triangle.area(), "\ntriangle_perimeter:", triangle.perimeter())

