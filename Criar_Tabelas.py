import sqlite3

banco = sqlite3.connect('Caixa_Eletronico.db')
cursor = banco.cursor()

#cursor.execute("CREATE TABLE id (nome text, idade integer, email text )")

cursor.execute("INSERT INTO id VALUES ('Silvio', 44, 'silvio.luiz@gmail.com')")

banco.commit()
#cursor.execute("SELECT * FROM id")
#print(cursor.fetchall())