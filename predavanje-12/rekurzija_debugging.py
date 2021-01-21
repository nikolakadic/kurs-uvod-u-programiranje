def factoriaal(n):
    if n == 1:
        return 1
    return n * factoriaal(n-1)


print(factoriaal(5))