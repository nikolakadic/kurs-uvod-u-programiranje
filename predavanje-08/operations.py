def addition(a,b):
    return a + b

def division(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Ne mozes dijeliti sa nulom, nauci matematiku')
        return a / 1
    finally:
        print('Zavrsio sam operaciju dijeljenja')

def sin(angle):
    """
    ...
    """
    return angle