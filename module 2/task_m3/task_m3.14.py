def fibonacci(n):
    return n if n == 1 or n == 0 else fibonacci(n-2)+fibonacci(n-1)


print(fibonacci(8))