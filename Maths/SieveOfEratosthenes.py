def primeNumbersTillN(n):
    prime_list = [True] * (n+1)
    prime_list[0] = False
    prime_list[1] = False

    i = 2
    while i*i <= n:
        if prime_list[i] == True:
            j = 2
            while i*j <= n:
                print(f"{i = }, {j = }")
                prime_list[i*j] = False
                j += 1
        i += 1

    prime_nos_till_n = [i for i, j in enumerate(prime_list) if j == True]
    print(f"{prime_nos_till_n}")


a = 50
primeNumbersTillN(a)