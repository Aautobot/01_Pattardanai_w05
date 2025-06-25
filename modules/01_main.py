import math

x = math.pi

def calculate_area(radius):
    """Calculate the area of a circle given its radius."""
    return math.pi * (radius ** 2)  
radius = float(input("Enter the radius of the circle: "))
area = calculate_area(radius)
print(f"The area of the circle with radius {radius} is: {area:.2f}")