from math import sqrt, pow

x1_coord = float(input("Enter the x coordinate of the first point "))
y1_coord = float(input("Enter the y coordinate of the first point"))
x2_coord = float(input("Enter the x coordinate of the second point"))
y2_coord = float(input("Enter the y coordinate of the second point"))

distance = round(sqrt(pow(x2_coord - x1_coord, 2) + pow(y2_coord - y1_coord, 2)), 2)

if distance < 5:
    print("Distance is less than five")
print(f"Distance is equal to {distance}")