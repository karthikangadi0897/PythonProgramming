def factorial(n):
    # Base case: 0! = 1
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))