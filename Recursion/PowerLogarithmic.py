def powerLogarithmic(x, n):
    if n == 1:
        return x
    pow_n_by_2 = powerLogarithmic(x, n//2)
    pow_n = pow_n_by_2 * pow_n_by_2
    if n % 2 == 1:
        pow_n *= x
    return pow_n

print(powerLogarithmic(3,5))