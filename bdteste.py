import mysql.connector

def create_connection():
    con = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'ceub123456'
    )
    print("Conexão", con)
    return con
def create_database():
    sql_create = '''CREATE DATABASE if not exists db_alunos'''
    cursor.execute(sql_create)
    sql_use = '''USE db_alunos'''
    cursor.execute(sql_use)
def create_table():
    sql = '''CREATE TABLE if not exists tb_chamada(
        idt INT NOT NULL AUTO_INCREMENT,
        nome VARCHAR(255) NOT NULL UNIQUE,
        ra INT(8) NOT NULL UNIQUE,
        data_ingress DATE NULL,
        PRIMARY KEY(idt)
        )'''
    cursor.execute(sql)
def insert():
    vnome = input("Digite o nome do aluno: ")
    vra = input("Digite o RA do aluno: ")
    vdtaIng = input("Digite a data de ingressão do aluno ao curso(yyyy-mm-dd): ")
    sql = f'''INSERT into tb_chamada
             (nome, ra, data_ingress)
             values('{vnome}', {vra}, '{vdtaIng}')'''
    cursor.execute(sql)
    conexao.commit()

def select_all():
    vbucet = input("Digite o nome do aluno para confirmar os dados: ")
    sql = f'''SELECT * from tb_chamada where nome = '{vbucet}' '''
    cursor.execute(sql)
    l_regs = cursor.fetchall()
    for l_reg in l_regs:
        print("------------")
        print(f"ID: {l_reg[0]}")
        print(f"Nome: {l_reg[1]}")
        print(f"RA: {l_reg[2]}")
        print(f"Data de ingressão: {l_reg[3]}")

def delete():
    valunodel = input("Digite o nome do aluno: ")
    sql = f'''DELETE from tb_chamada where nome = '{valunodel}' '''
    print(f"O aluno {valunodel} foi removido do sistema com sucesso: ")
    cursor.execute(sql)
    conexao.commit()

def update():
    valuno = input("Digite o nome do aluno para ter a data atualizada: ")
    vnovadata = input("Digite a nova data de ingressão do aluno(yyyy-mm-dd): ")
    sql = f'''UPDATE tb_chamada
            set data_ingress = '{vnovadata}'
            where nome = '{valuno}' '''
    cursor.execute(sql)
    conexao.commit()

def close_connection():
    cursor.close()
    conexao.close()
    print("Conexão Fechada")

def show_record():
    sql = f'''SELECT * from tb_chamada '''
    cursor.execute(sql)
    l_regs = cursor.fetchall()
    for l_reg in l_regs:
        print(f"-----{l_reg[0]}-------")
        print(f"ID: {l_reg[0]}")
        print(f"Nome: {l_reg[1]}")
        print(f"RA: {l_reg[2]}")
        print(f"Data de ingressão: {l_reg[3]}")


if __name__ == '__main__':
    conexao = create_connection()
    cursor = conexao.cursor()
    create_database()
    create_table()

    while True:
        print("-------Menu-------")
        print("[c] Adicionar Aluno")
        print("[r] Pesquisar Aluno")
        print("[u] Atualizar data de um aluno")
        print("[d] Remover um aluno")
        print("[p] Ver a chamada completa")
        print("[s] Sair")
        opc = input("Escolha uma das opções acima: ").lower()

        if opc == 'c':
            insert()
        elif opc == 'r':
            select_all()
        elif opc == 'u':
            update()
        elif opc == 'd':
            delete()
        elif opc == 'p':
            show_record()
        elif opc == 's':
            print("Operação finalizada")
            break
        else:
            print("Opção inválida, tente novamente")
    close_connection
