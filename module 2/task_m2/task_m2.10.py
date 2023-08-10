num = int(input("Enter integer (0 for output): "))
sum = 0
print(num)
while num != 0:
    for i in range(1, num+1):
        sum += i
        print(f'{sum}')
    num = int(input("Enter integer (0 for output): "))
