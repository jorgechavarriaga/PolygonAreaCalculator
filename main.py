import shape_calculator
from unittest import main

# Test Rectangle class & methods
rect = shape_calculator.Rectangle(10, 3)
print("Area: " + str(rect.get_area()))
rect.set_width(30)
rect.set_height(10)
print("Perimeter: " + str(rect.get_perimeter()))
print(rect)
print("Picture : \n\n" + rect.get_picture())

# Test Square class & methods
sq = shape_calculator.Square(9)
print("Area: " + str(sq.get_area()))
sq.set_side(15)
print("Diagonal: " + str(sq.get_diagonal()))
print(sq)
print("Picture: \n\n" + str(sq.get_picture()))



# Run unit tests automatically
main(module='test_module', exit=False)