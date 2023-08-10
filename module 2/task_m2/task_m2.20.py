number = int(input("Enter three-digit number: "))

hundred = number // 100
units = number % 10

if hundred == units:
    print("Is palindrome")
else:
    print("Not palindrome")