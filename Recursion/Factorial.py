def factorial(n):
    if n == 1:
        return 1
    fac_n_minus_1 = factorial(n-1)
    fac_n = n * fac_n_minus_1
    return fac_n

print(factorial(7))