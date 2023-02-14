import sqlite3
banco = sqlite3.connect('Caixa_Eletronico.db')
cursor = banco.cursor()

email = input('Digite o email do usuario que gostaria de EXCLUIR: ')

vsql ="DELETE  FROM id WHERE nome="+email
def deletar(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print('Registro Apagado!')

    except sqlite3.Error as erro:
        print(erro)

deletar(banco,vsql)