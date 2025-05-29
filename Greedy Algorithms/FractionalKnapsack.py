def fractionalKnapsack(item_list, knapsack):
    n = len(item_list)

    item_list.sort(key=lambda x: (-x[0],x[1]))
    print(f"{item_list = }")

    i = 0
    profits = 0

    while i < n and knapsack > 0:
        if item_list[i][1] <= knapsack:
            profits += item_list[i][0]
            knapsack -= item_list[i][1]
        else:
            curr_profit  = (item_list[i][0] * (knapsack/item_list[i][1]))
            profits += curr_profit
            knapsack = 0
        i += 1

    return profits


# list pf pairs of value and weight of items
items_1 = [[100, 20], [60, 10], [100, 50], [200, 50]]
bag_1 = 90

print(fractionalKnapsack(items_1, bag_1))
