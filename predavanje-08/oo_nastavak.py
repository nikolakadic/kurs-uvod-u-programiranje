class Ucenik():
    broj_ucenika = 10
    def __init__(self, ime, prezime, grad):
        self.ime = ime
        self.prezime = prezime
        self.grad = grad

    def __str__(self):
        return self.ime +", "+ self.prezime+", "+ self.grad

    def setIme(self,ime):
        if ime.isalpha():
            self.ime = ime
        else:
            self.ime = 'Neimenovan'

    def setGrad(self, grad): # Seter - funckija koja sluzi za kontrolisano podesavanje osobina objekta klase!
        if grad not in ['Lisabon', 'Podgorica', 'Beograd', 'Budva']:
            self.grad = 'Podgorica'
        else:
            self.grad = grad
    def getGrad(self):
        return 'Ucenik je iz ', self.grad, 'a'


ucenik1 = Ucenik('Marko', 'Markovic', 'Lisabon')

# ucenik1.setGrad('Lisabon')

# print(ucenik1.getGrad())

ucenik1.setIme('Petar')
print(ucenik1)

print(Ucenik.broj_ucenika)

# PRVO ZASTO 
# TEK ONDA KAKO!