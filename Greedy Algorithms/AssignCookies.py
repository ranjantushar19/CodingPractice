def assignCookies(hunger, cookies):
    '''
    Given a greed or hunger level of multiple children and
    bundles each containing certain no. of chocolates.
    Find the maximum numbers od children you can satisfy.

    Solution - sort both in ascending order.
    '''
    pass
    hunger.sort()
    m = len(hunger)
    cookies.sort()
    n = len(cookies)

    i = 0
    j = 0
    satisfied = 0
    while i < m and j < n:
        print(f"hunger : {hunger[i]}, cookies : {cookies[j]}")
        if hunger[i] <= cookies[j]:
            satisfied += 1
            i += 1
            j += 1
        else:
            j += 1

    return satisfied


hung = [1, 5, 3, 3, 4]
cook = [4, 2, 1, 2, 1, 3]

a = assignCookies(hung, cook)
print(f"{a = }")