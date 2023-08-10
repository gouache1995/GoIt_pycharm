string_one = input("Enter string: ")
string_two = input("Enter string to compare: ")

for char in string_one:
    if char not in string_two:
        print(False)
        break
else: print(True)