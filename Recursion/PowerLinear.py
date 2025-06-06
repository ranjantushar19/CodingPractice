def powerLinear(x, n):
    if n == 0:
        return 1
    pow_n_minus_1 = powerLinear(x, n-1)
    pow_n = x * pow_n_minus_1
    return pow_n

print(powerLinear(2,10))
