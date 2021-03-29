import math

# Rectangle class
class Rectangle:
    # When a Rectangle object is created, it should be initialized with `width` and `height` attributes.
    def __init__(self, width, height):
        self.width = width
        self.height = height

    #  If an instance of a Rectangle is represented as a string, it should look like: `Rectangle(width=5, height=10)`
    def __str__(self):
        rectangle_string = type(self).__name__ + "(width=" + str(self.width) + ", height=" + str(self.height) +")"
        return rectangle_string

    #  method set_width
    def set_width(self, width):
        self.width = width

    #  method set_height
    def set_height(self, height):
        self.height = height

    # method get_area
    def get_area(self):
        area = self.width * self.height
        return area

    # method get_perimeter
    def get_perimeter(self):
        perimeter = (2* (self.width + self.height))
        return perimeter

    # method get_diagonal
    def get_diagonal(self):
        diagonal = math.sqrt(pow(self.width, 2) + pow(self.height, 2))
        return diagonal

    # method get_picture
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'

        pattern = ''
        for index in range(self.height):
            for index in range(self.width):
                pattern += '*'
            pattern += '\n'
        return pattern
        
    # method get_amount_inside
    def get_amount_inside(self, shape):
        area1 = shape.get_area()
        count = 0
        area_home = self.get_area()
        while area_home >= area1:
            area_home = area_home - area1
            count += 1
        return count
    
# Square class: The Square class should be a subclass of Rectangle. When a Square object is 
# created, a single side length is passed in. The `__init__` method should store the side 
# length in both the `width` and `height` attributes from the Rectangle class.
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side,side)

    # An instance of a Square is represented as a string
    def __str__(self):
        square_string = type(self).__name__ + "(side="+ str(self.width) + ")"
        return square_string


    # method set_side
    def set_side(self, side):
        self.set_width(side)
        self.set_height(side)