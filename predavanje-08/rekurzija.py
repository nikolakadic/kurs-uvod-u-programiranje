def factorial(n):
    # Iterative / iterativno rješenje faktorijel
    rez = 1
    while n > 0:
        rez *= n
        n = n - 1 
    return rez

def factorial_rec(n):
    if n == 1: # TERMINALNI USLOV - dio svake rekurzije
        return 1
    return n*factorial_rec(n-1)



# print(factorial(5))

# 5! = 5*4*3*2*1

# n! = n*(n-1)*(n-2)*...*1

print(factorial_rec(5))

"""
5! = 5 * 4!

4! = 4 * 3!

"""