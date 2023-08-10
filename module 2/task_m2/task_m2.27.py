string = input("Enter sentence: ")

count_symbols = 0
count_a = 0
count_o = 0
count_t = 0
count_space = 0

for char in string:
    count_symbols += 1
    if char == 'a':
        count_a += 1
        continue
    if char == 'o':
        count_o += 1
        continue
    if char == 't':
        count_t += 1
        continue
    if char == ' ':
        count_space += 1

print(f"Count of symbols 'a' {count_a} - percentage in sentence {round((count_a/count_symbols)*100,2)}%")
print(f"Count of symbols 'o' {count_o} - percentage in sentence {round((count_o/count_symbols)*100,2)}%")
print(f"Count of symbols 't' {count_t} - percentage in sentence {round((count_t/count_symbols)*100,2)}%")
print(f"Count of words {count_space + 1}")