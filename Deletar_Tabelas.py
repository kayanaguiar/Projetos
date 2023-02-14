import sqlite3

try:

    banco = sqlite3.connect('Caixa_Eletronico.db')
    cursor = banco.cursor()

    cursor.execute("DELETE FROM id WHERE nome = 'Julia'")

    banco.commit()
    banco.close()
    print("Os dados foram excluidos com sucesso!")

except sqlite3.Error as erro:
    print("Erro ao excluir : ", erro)