a = int(input("Enter a: "))
b = int(input("Enter b: "))

if (a >= 1 and a <= 20) and (b >= 1 and b <= 20):
    sum = 0
    mul = 1

    for el in range(a, b + 1):
        sum = sum + el
        mul = mul * el

    print(f"Sum {sum}, product of numbers {mul}")
else:
    print("The numbers a and b must be between 1 and 20")