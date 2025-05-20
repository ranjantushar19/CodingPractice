def gasStation(gas, cost):
    n = len(gas)

    if sum(cost) > sum(gas):
        return -1

    total = 0
    idx = 0

    for i in range(n):
        total += (gas[i] - cost[i])
        if total < 0:
            total = 0
            idx = i+1

    return idx

gas1 = [1, 2, 3, 4, 5]
cost1 = [3, 4, 5, 1, 2]

print(gasStation(gas1, cost1))