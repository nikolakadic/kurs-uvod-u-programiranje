"""
"""

class Fruits:
    """ """
    
    count = 0 # staticka atribut klase
    
    def __init__(self, name, count):
        self.name = name
        self.count = count
        Fruits.count += count


apples = Fruits('apple', 10)
pears = Fruits('pear', 20)


print(getattr(apples,'count'))
setattr(pears, 'count', 200)

print(getattr(pears,'count'))
print(hasattr(pears,'name'))
