import sqlite3

banco = sqlite3.connect('Caixa_Eletronico.db')
cursor = banco.cursor()


def atualizar(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()

    except sqlite3.Error as erro:
        print(erro)
    finally:
        print('Registro atualizado!')
vsql = "UPDATE id SET dinheiro = 2000 WHERE nome = 'Cleber'"

atualizar(banco,vsql)