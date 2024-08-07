class Circle:
    def __init__(self, radius, color):
        self.__radius = float(radius)
        self.__color = color

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = float(radius)

    def get_color(self):
        return self.__color

    def set_color(self, color):
        self.__color = color

    def calculate_area(self):
        return 3.14 * self.__radius * self.__radius

    def calculate_perimeter(self):
        return 2 * 3.14 * self.__radius

# Global scope variables
my_radius = float(input("Enter the radius of the circle: "))
my_color = input("Enter the color of the circle: ")

def check_validity(radius, color):
    if radius <= 0:
        return False
    else:
        return Circle(radius, color)

# Store the object returned from check_validity into circle_obj
circle_obj = check_validity(my_radius, my_color)

if isinstance(circle_obj, Circle):
    # Calculate the area of the circle
    area = circle_obj.calculate_area()
    print(f"Area is: {area}")

    # Calculate the perimeter of the circle
    perimeter = circle_obj.calculate_perimeter()
    print(f"Perimeter is: {perimeter}")
else:
    print("Invalid Radius")
