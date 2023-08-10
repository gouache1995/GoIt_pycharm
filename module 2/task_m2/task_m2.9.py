first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))
gcd = first

while True:

    if first % gcd == 0 and second % gcd == 0:
        print(gcd)
        break
    gcd -= 1