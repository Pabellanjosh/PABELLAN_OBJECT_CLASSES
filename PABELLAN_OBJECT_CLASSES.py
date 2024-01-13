import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        area = math.pi * self.radius ** 2
        print("The area of the circle is:", area)

    def perimeter(self):
        perimeter = 2 * math.pi * self.radius
        print("The perimeter of the circle is:", perimeter)

# Create a Circle object with a radius of 5
circle = Circle(5)

# Calculate and print the area of the circle
circle.area()

# Calculate and print the perimeter of the circle
circle.perimeter()