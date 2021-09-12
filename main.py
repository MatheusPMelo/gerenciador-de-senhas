import sqlite3

senha_mestre = "123"

psd = input("Coloque a Senha Mestre: ")
if psd != senha_mestre:
    print("Senha Inválida. Saíndo...")
    exit()

conx = sqlite3.connect('passwords.db')

cursor = conx.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    service TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
''')

def menu():
    print("*******************************")
    print("# i -> Inserir uma nova senha #")
    print("# l -> Listar Contas Salvas   #")
    print("# r -> Recuperar uma Senha    #")
    print("# s -> Sair                   #")
    print("*******************************")

def get_pass(service):
    cursor.execute(f'''
        SELECT username, password FROM users
        WHERE service = '{service}'
    ''')

    if cursor.rowcount == 0:
        print("Serviço não castrado (use 'l' para verificar os serviços.")
    else: 
        for user in cursor.fetchall():
            print(user)

def insert_pass(service, username, password):
    cursor.execute(f'''

    INSERT INTO users (service, username, password)
    VALUES ('{service}', '{username}', '{password}')
    
    ''')
    conx.commit()

def show_services():
    cursor.execute('''
        SELECT service FROM users
    ''')
    for service in cursor.fetchall():
        print(service)

while True:
    menu()
    opr = input("O que você deseja fazer? ")


    if opr not in ['i', 'l', 'r', 's', 'I', 'L','R','S']:
        print("Opção inválida")
        continue

    if opr == 'i' or opr == 'I':
        serv = input('Qual nome do serviço? ')
        user = input('Qual o nome do usuário? ')
        psw = input('Qual a senha?')
        insert_pass(serv, user, psw)

    if opr == 'l' or opr == 'L':
        show_services()

    if opr == 'r' or opr == 'R':
        service = input ('Qual o serviço para o qual quer a senha? ')
        print ("USUÁRIO | SENHA")
        get_pass(service)
    
    
    if opr == "s" or opr == 'S':
        break

conx.close()