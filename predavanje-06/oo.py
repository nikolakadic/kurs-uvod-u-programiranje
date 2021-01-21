# klasa je sablon 
# objekat je jedan primjerak te klase

# klasa - sablon za stampanje betonskih cipela 
# objekat - jedna cipela

class Djecak:
    #konstruktor - funkcija koja stvara objekat
    def __init__(self, i, p, g):
        self.ime = i
        self.prezime = p
        self.godine = g


marko = Djecak('Marko', 'Prezime', 15)

print('MARKO:')
print(marko.ime, marko.prezime, marko.godine)


