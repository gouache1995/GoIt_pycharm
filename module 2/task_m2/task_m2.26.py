line = input("Enter string: ")
line = line.lower()

if line == line[::-1]:
    print("Is palindrome")
else:
    print("Not palindrome")