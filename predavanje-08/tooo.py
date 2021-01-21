"""
Pocetak sudoku
"""
print("IGRATE IGRU SUDOKU")
print("")
gametable = [
        [1, "", "","","","","","",8],
        ["", 2, "","","","","","",""],
        ["", "", 3,"","","","","",""],
        ["", "", "",4,"","","","",""],
        ["", "", "","",5,"","","",""],
        ["", "", "","","",6,"","",""],
        ["", "", "","","","",7,"",""],
        ["", "", "","","","","",8,""],
        [9, "", "","","","","","",1],
]
def print_gametable(gametable):
    print(gametable[0])
    print(gametable[1])
    print(gametable[2])
    print(gametable[3])
    print(gametable[4])
    print(gametable[5])
    print(gametable[6])
    print(gametable[7])
    print(gametable[8])
print_gametable(gametable)
limit = 10
game_end= False
unos = 0
while not game_end and unos < limit:
    print("Igrate!")
    unos = int(input("Unesite broj od 1 do 9:  "))
    print("Unesite koordinate: ")
    x = int(input())
    y = int(input())
    if gametable[x][y] == "":
        gametable[x][y] = unos
    else:
        while gametable[x][y] != "":
            print("Polje je vec popunjeno, unesite druge koordinate")
            x = int(input())
            y = int(input())
        gametable[x][y] = unos
    print_gametable(gametable)
else:
    print("Pogresan unos")