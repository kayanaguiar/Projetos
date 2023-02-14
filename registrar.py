import sqlite3

banco = sqlite3.connect('Caixa_Eletronico.db')
cursor = banco.cursor()

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')
email = input('Digite seu email: ')
dinheiro = input('Quanto gostaria de depositar: ')

vsql = "INSERT INTO id (nome, idade, email, dinheiro) VALUES ('"+nome+"', '"+idade+"', '"+email+"', '"+dinheiro+"')"
def inserir(conexao,sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print('Registro inserido!')

    except sqlite3.Error as erro:
        print(erro)

inserir(banco,vsql)