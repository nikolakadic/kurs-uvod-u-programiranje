# inheritance
# DRY = dont repeat yourself

class Animal():
    def __init__(self, name, breed, age, weight):
        self.name = name
        self.breed = breed
        self.age = age
        self.weight = weight
    
    def say_hello(self):
        print('Hello, my name is', self.name)
    
    def eat(self):
        print('Nom nom nom')
        self.weight+=0.5
    

class Dog(Animal): # subclass Dog, superclass Animal
    def __init__(self, name, breed, age, weight, strenght=11):
        super().__init__(name,breed,age, weight) # poziva se konstruktor superklase
        self.strenght = strenght


class Cat(Animal):
    def __init__(self, name, breed, age, weight, cuteness=100):
        super().__init__(name,breed,age, weight) # poziva se konstruktor superklase
        self.cuteness = cuteness

rex = Dog(name='Rex', breed='German sheperd', age=10, weight=15)
rex.say_hello()
rex.eat()


mica = Cat(name='Mica', breed='Persian', age=3, weight=4)
mica.say_hello()
mica.eat()

print(rex.weight)

print(isinstance(Cat, Animal)) # OBJEKAT - KLASA (da li je to objekat te klase)

print(issubclass(Animal, Cat))