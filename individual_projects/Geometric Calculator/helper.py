"""class shape
    atributes: name, dimensions, area, perimeter
    methods: calculate area, calculate perimeter
    define calculate area function
        if shape is circle
            area = pi * radius^2
        if shape is rectangle
            area = length * width
        if shape is triangle
            area = 0.5 * base * height
        subclass square from rectangle
            area = side^2
        subclass cube from square
            volume = side^3
        subclass sphere from circle
            volume = (4/3) * pi * radius^3
        subclass cylinder from circle
            volume = pi * radius^2 * height
    def calculate perieter function
        if shape is circle
            perimeter = 2 * pi * radius
        if shape is rectangle
            perimeter = 2 * (length + width)
        if shape is triangle
            perimeter = side1 + side2 + side3
        if shape is square
            perimeter = 4 * side
        if shape is cube
            perimeter = 12 * side
        if shape is sphere
            perimeter = 0
        if shape is cylinder
            perimeter = 2 * pi * radius + 2 * height
define new shape function
    ask user for shape type
    ask user for dimensions based on shape type
    create new shape object with given dimensions
    calculate area and perimeter for the new shape
    add new shape to library
define view shapes function
    if library is empty
        display "No shapes in library"
    else
        for each shape in library
            display shape name, dimensions, area, and perimeter
define compare shapes function
    ask user for first shape to compare
    ask user for second shape to compare
    if both shapes exist in library
        compare area and perimeter of both shapes
        display comparison results
    else        display "One or both shapes not found in library"
define select shape function
    ask user for shape name to select
    if shape exists in library
        display shape details (name, dimensions, area, perimeter)
    else
        display "Shape not found in library"
define sort shapes function
    ask user for sorting criteria (area or perimeter)
    if criteria is area
        sort shapes in library by area
    if criteria is perimeter
        sort shapes in library by perimeter
    display sorted shapes
define help function
    display instructions for using the geometric calculator
    explain how to create new shapes, view shapes, compare shapes, select shapes, and sort shapes
    provide examples of shape dimensions and calculations
    """
class Shape:
    def __init__(self, name, dime, type):
        self.name = type
        self.dime = dime
        self.area = self.calculate_area()
        self.perimeter = self.calculate_perimeter()
    def __str__(self):
        return f"{self.name.capitalize()} with dimensions {self.dime}, Area: {self.area}, Perimeter: {self.perimeter}"

    def calculate_area(self):
        if self.name == "circle":
            radius = self.dime['radius']
            return 3.14159 * radius ** 2
        if self.name == "rectangle":
            length = self.dime['length']
            width = self.dime['width']
            return length * width
        if self.name == "triangle":
            base = self.dime['base']
            height = self.dime['height']
            return 0.5 * base * height
        if self.name == "square":
            side = self.dime['side']
            return side ** 2
        if self.name == "cube":
            side = self.dime['side']
            return side ** 3
        if self.name == "sphere":
            radius = self.dime['radius']
            return (4/3) * 3.14159 * radius ** 3
        if self.name == "cylinder":
            radius = self.dime['radius']
            height = self.dime['height']
            return 3.14159 * radius ** 2 * height

    def calculate_perimeter(self):
        if self.name == "circle":
            radius = self.dime['radius']
            return 2 * 3.14159 * radius
        if self.name == "rectangle":
            length = self.dime['length']
            width = self.dime['width']
            return 2 * (length + width)
        if self.name == "triangle":
            side1 = self.dime['side1']
            side2 = self.dime['side2']
            side3 = self.dime['side3']
            return side1 + side2 + side3
        if self.name == "square":
            side = self.dime['side']
            return 4 * side
        if self.name == "cube":
            side = self.dime['side']
            return 12 * side
        if self.name == "sphere":
            return 0
        if self.name == "cylinder":
            radius = self.dime['radius']
            height = self.dime['height']
            return 2 * 3.14159 * radius + 2 * height
def new_shape():
    print ("creatig new shape")
    while True:
        shape_type = input("please enter the form of the shape.\n available forms are circle, rectangle, triangle, square, cube, sphere, and cylinder\n").lower().strip()
        if shape_type not in ["circle", "rectangle", "triangle", "square", "cube", "sphere", "cylinder"]:
            print ("invalid shape form")
        break
    if shape_type == "circle":
        print ("please enter the radius of your circle")
        radius = int(input().strip())
        print ("what would you like this circle to be called?")
        name = input("").strip().capitalize()
        new_circle = Shape(name, {"radius": radius}, "circle")
        with open("individual_projects/Geometric Calculator/shapes.csv", "a") as file:
            file.write(str(new_circle) + "\n")
    if shape_type == "rectangle":
        print ("please enter the length of your rectangle")
        length = int(input().strip())
        print ("please enter the width of your rectangle")
        width = int(input().strip())
        print ("what would you like this rectangle to be called?")
        name = input("").strip().capitalize()
        new_rectangle = Shape(name, {"length": length, "width": width} , "rectangle")
        with open("individual_projects/Geometric Calculator/shapes.csv", "a") as file:
            file.write(str(new_rectangle) + "\n")
    if shape_type == "triangle":
        print ("please enter the base of your triangle")
        base = int(input().strip())
        print ("please enter the height of your triangle")
        height = int(input().strip())
        print ("what would you like this triangle to be called?")
        name = input("").strip().capitalize()
        new_triangle = Shape(name, {"base": base, "height": height} , "triangle")
        with open("individual_projects/Geometric Calculator/shapes.csv", "a") as file:
            file.write(str(new_triangle) + "\n")
    if shape_type == "square":
        print ("please enter the side length of your square")
        side = int(input().strip())
        print ("what would you like this square to be called?")
        name = input("").strip().capitalize()
        new_square = Shape(name, {"side": side} , "square")
        with open("individual_projects/Geometric Calculator/shapes.csv", "a") as file:
            file.write(str(new_square) + "\n")
    if shape_type == "cube":
        print ("please enter the side length of your cube")
        side = int(input().strip())
        print ("what would you like this cube to be called?")
        name = input("").strip().capitalize()
        new_cube = Shape(name, {"side": side} , "cube")
        with open("individual_projects/Geometric Calculator/shapes.csv", "a") as file:
            file.write(str(new_cube) + "\n")
    if shape_type == "sphere":
        print ("please enter the radius of your sphere")
        radius = int(input().strip())
        print ("what would you like this sphere to be called?")
        name = input("").strip().capitalize()
        new_sphere = Shape(name, {"radius": radius} , "sphere")
        with open("individual_projects/Geometric Calculator/shapes.csv", "a") as file:
            file.write(str(new_sphere) + "\n")
    if shape_type == "cylinder":
        print ("please enter the radius of your cylinder")
        radius = int(input().strip())
        print ("please enter the height of your cylinder")
        height = int(input().strip())
        print ("what would you like this cylinder to be called?")
        name = input("").strip().capitalize()
        new_cylinder = Shape(name, {"radius": radius, "height": height} , "cylinder")
        with open("individual_projects/Geometric Calculator/shapes.csv", "a") as file:
            file.write(str(new_cylinder) + "\n")
def view_shapes():
    with open("individual_projects/Geometric Calculator/shapes.csv", "r") as file:
        shapes = file.readlines()
        if not shapes:
            print ("no shapes in library")
        else:
            for shape in shapes:
                #FIIIIIXXXX THIS!!!!!
                pass

def compare_shapes():
    pass
def select_shape():
    pass
def sort_shapes():
    pass
def helps():
    pass
