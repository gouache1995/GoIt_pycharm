k = int(input("Enter k: "))
l = int(input("Enter l: "))

if k != l:
    if k < l:
        k = l
    else:
        l = k
else:
    k, l = 0, 0

print(f"k equal to {k} , l equal to {l}")