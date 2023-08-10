def factorial(n):
    """Функція для обчислення факторіалу числа n."""
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def number_of_groups(n, k):
    """Функція для обчислення кількості різних списків переможців при розіграші."""
    if n < k:
        return 0
    else:
        number = factorial(n)
        number2 = factorial(k) * factorial(n - k)
        return number // number2

n = 50
k = 7
result = number_of_groups(n, k)
print(result)