def printRecursion(n):
    if n == 0:
        return
    
    print(n)
    printRecursion(n-1)


printRecursion(7)
