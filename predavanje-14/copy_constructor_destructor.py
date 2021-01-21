import copy

class Dog:
    # konstruktor
    def __init__(self, name, breed, age, color):
        self.name = name
        self.breed = breed
        self.age = age
        self.color = color

    def __repr__(self):
        return f'{self.name}, {self.breed}, {self.age}, {self.color}'


rex = Dog('Rex','German sheperd', 15, 'brown')
# DEEP COPY
# SHALLOW COPY


leo = copy.deepcopy(rex)

del rex

leo.name='Leo'

# print(rex)
print(leo)


l1 = [1,2,3,4,5,6]
l2 = copy.deepcopy(l1)

l2.append(8)

print(l2)

# Garbage collector
# Memory leak