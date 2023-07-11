num = int(input("Введіть число від 0 до 100: "))
sum = 0
current_num = 0

while current_num <= num:
    sum += current_num
    current_num += 1

print("Сума чисел від 0 до", num, "включно:", sum)
