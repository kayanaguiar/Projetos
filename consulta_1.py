import sqlite3

banco = sqlite3.connect('Caixa_Eletronico.db')
cursor = banco.cursor()


def consulta(conexao,sql):
    c=conexao.cursor()
    c.execute(sql)
    resultado = c.fetchall()
    return resultado

vsql = "SELECT * FROM id WHERE nome = 'Cleber'"
res = consulta(banco,vsql)
for r in res:
    print(r)