import sqlite3

connection = sqlite3.connect('veterinarska_ustanova_pet_uvod.db')

cursor = connection.cursor()

# cursor.execute('''CREATE TABLE zaposleni
            #  (licenca text, ime text, prezime text)''') 

# cursor.execute("INSERT INTO zaposleni VALUES ('2002022','Stefan','Jankovic')")

# connection.commit()

result_rows = cursor.execute("""SELECT UPPER(ime) FROM zaposleni where ime='Stefan'""")

for row in result_rows:
    print(row)

connection.close()
# context manager (with .. file .. db)