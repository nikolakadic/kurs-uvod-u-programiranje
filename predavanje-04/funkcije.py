def saberi(a, b):
    c = a + b
    print('tetstest1')
    return c
    print('tetstest2')

def oduzmi(c, d):
    r = c - d
    return r

def pomnozi(a, b):
    c = a * b
    return c

# racunanje (5+4) + (10-5) * (5*5)
#              9    +   5 *  25
#              9    +    125
#              134      
racunanje = saberi(5,4) + oduzmi(10,5) * pomnozi(5,5)
