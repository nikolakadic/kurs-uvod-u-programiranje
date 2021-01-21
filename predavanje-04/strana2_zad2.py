n = int(input('Unesite zeljeni broj '))

prva_cifra = n//100
srednja_cifra = (n//10)%10
posljednja_cifra = n%10


def odstampaj_najveci_od_tri_broja(prva, druga, treca):
    if prva > druga and prva > treca:
        return prva
    elif druga > prva and druga > treca:
        return druga
    else:
        return treca

rezultat = odstampaj_najveci_od_tri_broja(prva_cifra, srednja_cifra, posljednja_cifra)
# Odstampamo petostruko uvecanu najvecu cifru
uvecani_rezultat = rezultat * 5
print(uvecani_rezultat)
