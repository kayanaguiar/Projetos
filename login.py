nome = input('Qual seu nome?'  )
print('Bem-vindo ao Banco do Embaixador,', nome,)

decisao = input('O que você gostaria de fazer: Logar, Registrar ou Sair?')

if decisao == "Logar":
    print('Você ira fazer login')
    import sqlite3 as db
    banco = db.connect('Caixa_Eletronico.db')
    login = input('Digite seu email')
    dados = banco.cursor()
    dados.execute('SELECT * FROM id WHERE email == login')
    if login == dados.email:
        print('Login realizado')
    
    
    





elif decisao == "Registrar":
    print('Você ira criar sua conta')
#Descobrir como fazer registro no bd
elif decisao == "Sair":
    print('Saindo...')
