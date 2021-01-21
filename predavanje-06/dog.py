class Dog:
    def __init__(self, name, age, breed, food, color):
        self.name = name
        self.age = age
        self.breed = breed
        self.food = food
        self.color = color

    # FUNKCIJA != PROCEDURA != METODA
    # METODA / METOD / METHOD
    def likes_meat(self):
        # Does dog like meat
        return self.food=='meat'

    def say_smth(self):
        print(self.name, 'says woof!')
    
    def say_your_name_and_age(self):
        print("I'm", self.name,"and I'm", self.age, "years old.")

# instanca je isto sto i objekat (sinonimi)

rex = Dog('Rex',10,'German sheperd','burek','brown')
aron = Dog('Aron',5,'Labrador','meat','yellow')
nora = Dog('Nora',11,'Retriever','meat','golden')

print(rex.age)
print(aron.age)
print(nora.age)

def older_dog(dog1, dog2):
    if dog1.age > dog2.age:
        print('The',dog1.name,'is older')
    elif dog1.age == dog2.age:
        print('The dogs are the same age')
    else:
        print('The',dog2.name,'is older')


older_dog(rex,aron)
older_dog(nora,rex)

print(rex.likes_meat(), aron.likes_meat(), nora.likes_meat())

rex.say_smth()
nora.say_smth()
aron.say_smth()


aron.say_your_name_and_age()