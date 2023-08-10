def power(base, exponent):
    if exponent == 0:
        return 1
    else:
        return base * power(base, exponent-1)


print(power(2,8))
print(pow(2,3))