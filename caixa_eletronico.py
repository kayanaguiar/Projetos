import os
import sqlite3

#Coneção com o banco
banco = sqlite3.connect('Caixa_Eletronico.db')
cursor = banco.cursor()

def query(conexao,sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except sqlite3.Error as ex:
        print(ex)
    finally:
        print('Operação finalizada, obrigado por utilizar o Banco do Embaixador')
        #conexao.close()

def consultar(conexao,sql):
    c = conexao.cursor()
    c.execute(sql)
    res = c.fetchall()
    #conexao.close
    return res





def menuPrincipal():
    nome = input('Qual seu nome?'  )
    print('Bem-vindo ao Banco do Embaixador,', nome,)
    os.system('pause')
    os.system("cls")
    print('1 - Criar conta')
    print('2 - Conferir saldo')
    print('3 - Atualizar dados')
    print('4 - Apagar conta')
    print('5 - Sair')

def Criarconta():
    os.system('cls')
    nome = input('Digite seu nome: ')
    idade = input('Digite sua idade: ')
    email = input('Digite seu email: ')
    dinheiro = input('Digite quanto deseja depositar: ')
    vsql = "INSERT INTO id (nome, idade, email, dinheiro) VALUES ('"+nome+"', '"+idade+"','"+email+"','"+dinheiro+"')"
    query(banco,vsql)

def Conferirsaldo():
     os.system('cls')
     nome = input('Digite seu nome: ')
     vsql = "SELECT dinheiro FROM id WHERE nome = '" + nome +"'"
     res = consultar(banco,vsql)
     if res:
        for linha in res:
             print("Saldo disponível: R$", linha[0])
             os.system('pause')
     else:
             print("Não foi encontrado saldo para o nome digitado.")
             os.system('pause')

def Atualizardados():
    os.system('cls')
    vid = input('Digite o nome que gostaria de alterar os dados: ')
    r = consultar(banco,"SELECT * FROM id WHERE nome LIKE '%"+vid+"%'")
    rnome = r [0][0]
    ridade = r [0][1]
    remail = r [0][2]
    rsaldo = r [0][3]
    vnome = input('Digite o novo nome:')
    vidade = input('Digite a nova idade: ')
    vemail = input('Digite o novo email: ')
    #vsaldo = input('Digite o saldo: ')
    vsaldo_input = input('Digite o saldo (use + para adicionar e - para subtrair), obrigatoria a atualização de saldo!: ')
    vsaldo = rsaldo + float(vsaldo_input[1:]) if vsaldo_input.startswith('+') else rsaldo - float(vsaldo_input[1:])
    if (len(vnome)==0):
        vnome = rnome
    if (len(vidade)==0):
        vidade = str(ridade)
    if (len(vemail)==0):
        vemail = remail
    #if (len(vsaldo)==0):
        #vsaldo = str(rsaldo)
    vsql = "UPDATE id SET nome= '"+vnome+"', idade='"+vidade+"', email='"+vemail+"', dinheiro='"+str(vsaldo)+"'WHERE nome = '"+vid+"'"
    query(banco,vsql) 




def Apagarconta():
     os.system('cls')
     nome = input('Digite o nome do usuario que deseja excluir permanentemente! ')
     vsql = "DELETE FROM id WHERE nome = '"+nome+"'"
     query(banco,vsql)


opc = 0
while opc !=5:
    menuPrincipal()
    opc = int(input('Digite uma opção: '))
    if opc == 1:
        Criarconta()
    elif opc == 2:
        Conferirsaldo()
    elif opc == 3:
        Atualizardados()
    elif opc == 4:
        Apagarconta()
    elif opc == 5:
        os.system('cls')
        print('Obrigado por utilizar o Banco do Embaixador')
    
    else:
        os.system('cls')
        print('opção invalida')
        os.system('pause')

#banco.close()
os.system('pause')