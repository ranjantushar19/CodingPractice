def toh(n, A, B, C):
    if n == 0:
        return

    toh(n-1, A, C, B)
    print(f"{n} : {A}  --->  {B}")
    toh(n-1, C, B, A)

toh(3, "A", "B", "C")