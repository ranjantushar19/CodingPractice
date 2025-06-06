def printZigZag(n):
    if n == 0:
        return
    print(f"Pre {n}")
    printZigZag(n-1)
    print(f"In {n}")
    printZigZag(n-1)
    print(f"Post {n}")

printZigZag(3)