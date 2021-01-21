# tekst zadatka... 

uneseni_broj = int(input('Unesite zeljeni broj '))

srednja_cifra = (uneseni_broj//10)%10

if srednja_cifra % 2 == 0:
    print('Srednja cifra je parna')
else:
    print('Srednja cifra je neparna')

print(srednja_cifra)