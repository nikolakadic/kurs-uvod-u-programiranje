"""Naming best practices"""

def sabiranje(sabirak_1, sabirak_2):
    """
    Makes addition of two arguments.

    sabirak_1: integer argument
    sabirak_2: integer argument
    returns: addition between two arguments
    """
    return sabirak_1 + sabirak_2

if __name__=="__main__":
    ZBIR = sabiranje(2,5)
    print(ZBIR)

print(__name__)

# Bezbjedan od bugova ~testiranje
# Lak za razumijevanje/citanje
# Spreman za izmjene