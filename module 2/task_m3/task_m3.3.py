def fibonachi(n):
    return n if n == 1 or n == 0 else fibonachi(n - 2) + fibonachi(n - 1)


print(fibonachi(8))

def factorial(n):
    if n == 0 or n == 1:
        return n
    else:
        return n * factorial(n-1)

    
print(factorial(5))
