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
import math
def input_validation(prompt, valid_options):
    while True:
        choice = input(prompt).strip().lower()
        if choice in valid_options:
            return choice
        else:
            print(f"Invalid choice. Please enter one of the following: {', '.join(valid_options)}")
class circle:
    def __init__(self, radius, name):
        self.radius = radius
        self.name = name
    def area(self):
        return 3.14159 * self.radius ** 2
    def perimeter(self):
        return 2 * 3.14159 * self.radius
    def __str__(self):
        return f"Circle; {{'radius': {self.radius}, 'name': {self.name}}}; area: {self.area()}; perimeter: {self.perimeter()}"

class rectangle:
    def __init__(self, length, width, name):
        self.length = length
        self.width = width
        self.name = name
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)
    def __str__(self):
        return f"Rectangle; {{'length': {self.length}, 'width': {self.width}}}; area: {self.area()}; perimeter: {self.perimeter()}"

class triangle:
    def __init__(self, base, height, name):
        self.base = base
        self.height = height
        self.name = name
    def area(self):
        return 0.5 * self.base * self.height
    def perimeter(self):
        side1 = math.sqrt((self.base / 2) ** 2 + self.height ** 2)
        side2 = side1
        side3 = self.base
        return side1 + side2 + side3
    def __str__(self):
        return f"Triangle; {{'base': {self.base}, 'height': {self.height}, 'name': {self.name}}}; area: {self.area()}; perimeter: {self.perimeter()}"

class square(rectangle):
    def __init__(self, side, name):
        super().__init__(side, side, name)
    def __str__(self):
        return f"Square; {{'side': {self.length}, 'name': {self.name}}}; area: {self.area()}; perimeter: {self.perimeter()}"

class cube(square):
    def __init__(self, side, name):
        super().__init__(side, name)
    def area(self):
        return 6 * self.side ** 2
    def perimeter(self):
        return 12 * self.side
    def __str__(self):
        return f"Cube; {{'side': {self.length}, 'name': {self.name}}}; area: {self.area()}; perimeter: {self.perimeter()}"

class sphere(circle):
    def __init__(self, radius, name):
        super().__init__(radius, name)
    def area(self):
        return 4 * 3.14159 * self.radius ** 2
    def perimeter(self):
        return 0
    def __str__(self):
        return f"Sphere; {{'radius': {self.radius}, 'name': {self.name}}}; area: {self.area()}; perimeter: {self.perimeter()}"

class cylinder(circle):
    def __init__(self, radius, height, name):
        super().__init__(radius, name)
        self.height = height
    def area(self):
        return 2 * 3.14159 * self.radius * self.height + 2 * 3.14159 * self.radius ** 2
    def perimeter(self):
        return 2 * 3.14159 * self.radius + 2 * self.height
    def __str__(self):
        return f"Cylinder; {{'radius': {self.radius}, 'height': {self.height}, 'name': {self.name}}}; area: {self.area()}; perimeter: {self.perimeter()}"

def new_shape():
    print ("creatig new shape")
    while True:
        shape_type = input("please enter the form of the shape.\n available forms are circle, rectangle, triangle, square, cube, sphere, and cylinder\n").lower().strip()
        if shape_type not in ["circle", "rectangle", "triangle", "square", "cube", "sphere", "cylinder"]:
            print ("invalid shape form")
        break
    if shape_type == "circle":
        print ("please enter the radius of your circle")
        while True:
            try:
                radius = int(input().strip())
                if radius <= 0:
                    print ("invalid input. please enter a positive number.")
                else:
                    break
            except ValueError:
                print ("invalid input. please enter a number.")
        print ("what would you like this circle to be called?")
        name = input("").strip().capitalize()
        new_circle = circle(radius, name)
        with open("individual_projects/Geometric Calculator/shapes.csv", "a") as file:
            file.write(str(new_circle) + "\n")
    if shape_type == "rectangle":
        while True:
            print ("please enter the length of your rectangle")
            try:
                length = int(input().strip())
            except ValueError:
                print ("invalid input. please enter a number.")
                continue
            if length <= 0:
                print ("invalid input. please enter a positive number.")
            else:
                break
        while True:
            print ("please enter the width of your rectangle")
            try:
                width = int(input().strip())
            except ValueError:
                print ("invalid input. please enter a number.")
                continue
            if width <= 0:
                print ("invalid input. please enter a positive number.")
            else:
                break 
        print ("what would you like this rectangle to be called?")
        name = str(input("").strip().capitalize())
        new_rectangle = rectangle(length, width, name)
        with open("individual_projects/Geometric Calculator/shapes.csv", "a") as file:
            file.write(str(new_rectangle) + "\n")
    if shape_type == "triangle":
        while True:
            try:
                print ("please enter the base of your triangle")
                base = int(input().strip())
                if base <= 0:
                    print ("invalid input. please enter a positive number.")
                    continue
                else:
                    break
            except ValueError:
                print ("invalid input. please enter a number.")
        while True:
            print ("please enter the height of your triangle")
            height = int(input().strip())
            if height <= 0:
                print ("invalid input. please enter a positive number.")
                continue
            else:
                break
        print ("what would you like this triangle to be called?")
        name = input("").strip().capitalize()
        new_triangle = triangle(base,height,name)
        with open("individual_projects/Geometric Calculator/shapes.csv", "a") as file:
            file.write(str(new_triangle) + "\n")
    if shape_type == "square":
        while True:
            print ("please enter the side length of your square")
            try:
                side = int(input().strip())
                if side <= 0:
                    print ("invalid input. please enter a positive number.")
                    continue
                else:
                    break
            except ValueError:
                print ("invalid input. please enter a number.")
        print ("what would you like this square to be called?")
        name = input("").strip().capitalize()
        new_square = square(side, name)
        with open("individual_projects/Geometric Calculator/shapes.csv", "a") as file:
            file.write(str(new_square) + "\n")
    if shape_type == "cube":
        while True:
            print ("please enter the side length of your cube")
            try:
                side = int(input().strip())
                if side <= 0:
                    print ("invalid input. please enter a positive number.")
                    continue
                else:
                    break
            except ValueError:
                    print ("invalid input. please enter a number.")
        print ("what would you like this cube to be called?")
        name = input("").strip().capitalize()
        new_cube = cube(side, name)
        with open("individual_projects/Geometric Calculator/shapes.csv", "a") as file:
            file.write(str(new_cube) + "\n")
    if shape_type == "sphere":
        while True:
            try:                
                print ("please enter the radius of your sphere")
                radius = int(input().strip())
                if radius <= 0:
                    print ("invalid input. please enter a positive number.")
                    continue
                else:
                    break
            except ValueError:
                print ("invalid input. please enter a number.")
        print ("what would you like this sphere to be called?")
        name = input("").strip().capitalize()
        new_sphere = sphere(radius, name)
        with open("individual_projects/Geometric Calculator/shapes.csv", "a") as file:
            file.write(str(new_sphere) + "\n")
    if shape_type == "cylinder":
        while True:             
            try:
                print ("please enter the radius of your cylinder")                
                radius = int(input().strip())                
                if radius <= 0:
                    print ("invalid input. please enter a positive number.")
                    continue
                else:
                    break
            except ValueError:
                print ("invalid input. please enter a number.")
        print ("please enter the height of your cylinder")
        height = int(input().strip())
        print ("what would you like this cylinder to be called?")
        name = input("").strip().capitalize()
        new_cylinder = cylinder(radius, height, name)
        with open("individual_projects/Geometric Calculator/shapes.csv", "a") as file:
            file.write(str(new_cylinder) + "\n")
def view_shapes():
    with open("individual_projects/Geometric Calculator/shapes.csv", "r") as file:
        shapes = file.readlines()
        if not shapes:
            print ("no shapes in library")
        else:
            for shape in shapes:
                for x in shape.split(";"):
                    if "{" in x:
                        for symbol in x:
                            if symbol == "\"" or symbol == "\'" or symbol == "{" or symbol == "}":
                                index_to_remove = x.index(symbol)
                                x = x[:index_to_remove] + x[index_to_remove+1:]
                        print(x)
                    else:                        
                        print (x.strip())
def compare_shapes():
    with open("individual_projects/Geometric Calculator/shapes.csv", "r") as file:
        shapes = file.readlines()
        for shape in shapes:

            print(shape.split(';')[0].strip())
    shape1_name = input("Please enter the name of the first shape: ").strip().capitalize()
    shape2_name = input("Please enter the name of the second shape: ").strip().capitalize()
    with open("individual_projects/Geometric Calculator/shapes.csv", "r") as file:
        shapes = file.readlines()
        for shape in shapes:
            if shape1_name in shape:
                shape1 = shape
            if shape2_name in shape:
                shape2 = shape
    if shape1 and shape2:
        print(f"Comparing {shape1_name} and {shape2_name}:")
        shape1_area = float(shape1.split(";")[2].split(":")[1].strip())
        shape1_perimeter = float(shape1.split(";")[3].split(":")[1].strip())
        shape2_area = float(shape2.split(";")[2].split(":")[1].strip())
        shape2_perimeter = float(shape2.split(";")[3].split(":")[1].strip())
        if shape1_area > shape2_area:
            print(f"{shape1_name} has a greater area than {shape2_name}.")
        elif shape1_area < shape2_area:
            print(f"{shape2_name} has a greater area than {shape1_name}.")
        else:
            print ("the shapes have the same perimeter")
        if shape1_perimeter > shape2_perimeter:
            print (f"{shape1_name} has a larger perimeter than {shape2_name}")
        elif shape2_perimeter > shape1_perimeter:
            print(f"{shape2_name} has a larger perimeter than {shape1_name}")
        else:
            print ("the two shapes have th same name")
    else:
        print("shapes not found.")
def select_shape():
    shapes_dict = {}
    with open("individual_projects/Geometric Calculator/shapes.csv", "r") as file:
        shapes = file.readlines()
        for shape in shapes:
            name = shape.split(",")[0].strip()
            shapes_dict[name] = shape
    shape_name = input("Please enter the name of the shape you want to select: ").strip().capitalize()
    if shape_name in shapes_dict:
        shape = shapes_dict[shape_name]
        print ("would you like to edit this shape? (y/n)")
        choice = input().strip().lower()
        if choice == "y":
            with open("individual_projects/Geometric Calculator/shapes.csv", "r") as file:
                lines = file.readlines()
            with open("individual_projects/Geometric Calculator/shapes.csv", "w") as file:
                for line in lines:                    
                    if line.strip() != shape.strip():
                        file.write(line)
            new_shape()
        else:
            for sect in shape.split(","):
                if isinstance(sect, dict):
                    print ("Dimensions:")
                    for key, value in eval(sect).items():
                        print (f"  {key}: {value}")
                else:
                    print (sect.strip())
def sort_shapes():
    sort_choice = input("would you like to sort the shapes by area or perimeter? ").strip().lower()
    with open("individual_projects/Geometric Calculator/shapes.csv", "r") as file:
        shapes = file.readlines()
        shapes_list = []
        for shape in shapes:
            name = shape.split(",")[0].strip()
            dimensions = eval(shape.split(";")[1].strip())
            area = float(shape.split(";")[2].split(":")[1].strip())
            perimeter = float(shape.split(";")[3].split(":")[1].strip())
            shapes_list.append({"name": name, "dimensions": dimensions, "area": area, "perimeter": perimeter})
        if sort_choice == "area":
            sorted_shapes = sorted(shapes_list, key=lambda x: x['area'])
        elif sort_choice == "perimeter":
            sorted_shapes = sorted(shapes_list, key=lambda x: x['perimeter'])
        else:
            print ("invalid sort choice")
            return
        for shape in sorted_shapes:
            print (f"{shape['name']} - Area: {shape['area']}, Perimeter: {shape['perimeter']}")
def helps():
    print ("Welcome to the Geometric Calculator! this tool allows you to create and modify varios shapes,\n view their dimensions, area, and perimeter, and compare and sort them based on these attributes.")
    print ("To create a new shape, select New Shape from the menu and follow the prompts to enter the shape type and its dimensions. \nYou can create circles, rectangles, triangles, squares, cubes, spheres, and cylinders.")
    print ("To view all the shapes in your library, select View Shapes from the menu. \nThis will display the name, dimensions, area, and perimeter of each shape you have created.")
    print ("To compare two shapes, select 'Compare' from the menu.")
