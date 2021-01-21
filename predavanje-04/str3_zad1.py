def broj_poz_neg():
    brojac_pozitivnih = 0
    brojac_negativnih = 0


    uneseni_broj = int(input('Unesite prvi broj '))
    while uneseni_broj != 0:
        if uneseni_broj > 0:
            brojac_pozitivnih = brojac_pozitivnih + 1
        else:
            brojac_negativnih = brojac_negativnih + 1
        uneseni_broj = int(input('Unesite sljedeci broj '))
    print('Kraj unosa.')
    print('Broj pozitivnih ', brojac_pozitivnih)
    print('Broj negativnih ',brojac_negativnih)
    

broj_poz_neg()
    