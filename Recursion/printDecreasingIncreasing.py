def printDecreasingIncreasing(n):
    if n == 0:
        return
    print(n)
    printDecreasingIncreasing(n-1)
    print(n)

printDecreasingIncreasing(5)

'''
print increasing decreasing can't be done using similar technique.
We can't break recursive call in middle to insert values.

pid(4) = 1 2 3 4 4 3 2 1
pid(3) = 1 2 3 3 2 1
 
'''