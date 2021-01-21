class Ucenik():
    def __init__(self, ime, prezime, grad):
        self.ime = ime
        self.prezime = prezime
        self.grad = grad

    def __str__(self):
        return self.ime +", "+ self.prezime+", "+ self.grad

baza_ucenika = open('demofile.txt','r')

niz_objekata_ucenika = []

lines_of_file = baza_ucenika.readlines()

i = 0

while i < len(lines_of_file):

    curr_name = lines_of_file[i]
    curr_surname = lines_of_file[i+1]
    curr_city = lines_of_file[i+2]

    curr_student = Ucenik(curr_name,curr_surname,curr_city) 

    niz_objekata_ucenika.append(curr_student)

    i += 3

for ucenik in niz_objekata_ucenika:
    print(ucenik)