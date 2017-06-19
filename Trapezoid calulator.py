print("This program calculates the area of a trapezoid")

trapezoid_height = input("Enter Trapezoid Height:")
trapezoid_height = float(trapezoid_height)

trapezoid_top = input("Enter Trapezoid Top Length:")
trapezoid_top = float(trapezoid_top)

trapezoid_bottom = input("Enter Trapezoid Bottom Lenght:")
trapezoid_bottom = float(trapezoid_bottom)

area = 1 / 2 * (trapezoid_top + trapezoid_bottom) * trapezoid_height
print("Area of The Trapezoid Is:",area)