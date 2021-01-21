a = 5
b = 0

# <, >, ==, !=, and, or, not 

while b < a:
    #print('Poceo sam da izvrsavam tijelo petlje')
    b = b + 1
    #print('b je sada ', b)

# 1 - inicijalna vrijednost brojaca - range[0]
# provjera uslova                    < range [posljednji clan niza]
# povecava brojac                     brojac = brojac + 1

# range(n) - ova ugradjena funkcija vraca [0, 1, 2, 3, 4, 5 ... n-1]
# range(5) = ova funkcija vraca [0, 1, 2, 3, 4]

for brojac in range(5):
    print(brojac)


zid_crn = False
zid_bijele_boje = True

print(zid_bijele_boje)

if zid_crn and 5 > 4:
    print('Zid je crn')
else: 
    print('Zid je bijele boje')

#print('Ovo je nakon petlje')