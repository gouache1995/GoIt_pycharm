from math import sqrt, pow
triangle_type = None

side1 = float(input("Enter first side of triangle: "))
side2 = float(input("Enter second side of triangle: "))
side3 = float(input("Enter third side of triangle: "))

if (side1 + side2) > side3 and (side1 + side3) > side2 and (side3 + side2) > side1:

    if side1 == side2 and side3 == side2 and side3 == side1:
        triangle_type = "equilateral"
    elif side1 == side2 or side3 == side2 or side1 == side3:
        triangle_type = "isosceles"
    elif sqrt(pow(side1, 2) + pow(side2,2)) == side3 or\
        sqrt(pow(side1, 2) + pow(side3, 2)) == side2 or\
        sqrt(pow(side3, 2) + pow(side2, 2)) == side1:
        triangle_type = "right-angled"
    else:
        triangle_type = "differential"

    print(triangle_type)
else:
    print("Not triangle")