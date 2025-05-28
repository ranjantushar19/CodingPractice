coin_denominations = [1, 2, 5, 10, 20, 50, 100, 500, 1000]

def minCoinsForChange(amount):
    num_coins = 0

    j = len(coin_denominations) - 1
    while amount > 0:
        if coin_denominations[j] > amount:
            j -= 1
        else:
            amount -= coin_denominations[j]
            num_coins += 1

    return num_coins



amount_1 = 70
print(minCoinsForChange(amount_1))

amount_2 = 131
print(minCoinsForChange(amount_2))