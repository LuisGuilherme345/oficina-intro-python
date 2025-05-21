import mysql.connector
from Scripts.mysqlallinonfile import delete


def create_connection():
    con = mysql.connector.connect(
        host='localhost',
        user='root',
        password='ceub123456',
    )
    print("Conexão", con)
    return con

def create_database():
    sql_create = '''CREATE DATABASE if not exists db_cadastro'''
    cursor.execute(sql_create)
    sql_use = "use db_cadastro"
    cursor.execute(sql_use)

def create_table():
    sql_cargo = '''CREATE TABLE if not exists tb_cargo(
       idt INT  NOT NULL AUTO_INCREMENT ,
       nome VARCHAR(255) NOT NULL UNIQUE,
       PRIMARY KEY (idt)
       )'''
    cursor.execute(sql_cargo)
    sql_empre = '''CREATE TABLE if not exists tb_empregado(
        idt INT  NOT NULL AUTO_INCREMENT,
        nome VARCHAR(255) NOT NULL UNIQUE,
        data_nasc DATE NULL,
        genero ENUM('M', 'F') NOT NULL,
        cod_cargo INT NOT NULL,
        PRIMARY KEY(idt),
        FOREIGN KEY(cod_cargo) REFERENCES tb_cargo(idt)
    )'''
    cursor.execute(sql_empre)

def insert_cargo():
    vnomecar = input("Digite o nome do cargo: ")

    sql = f'''INSERT INTO tb_cargo
            (nome)
            values('{vnomecar}')'''

    cursor.execute(sql)
    conexao.commit()

def insert_empregado():
    vnomeempregado = input("Digite o nome do empregado: ")
    vdatanasc = input("Digite a data de nascimento do empregado (yyyy-mm-dd): ")
    vgenero = input("Digite o genero do empregado (M/F): ")
    vcargo = input("Digite o código do cargo do empregado: ")

    sql = f'''INSERT INTO tb_empregado
                (nome, data_nasc, genero, cod_cargo)
                values('{vnomeempregado}', '{vdatanasc}', '{vgenero}', {vcargo})'''

    cursor.execute(sql)
    conexao.commit()

def select_all_cargo():
    sql = '''SELECT * FROM tb_cargo'''
    cursor.execute(sql)
    l_registros = cursor.fetchall()
    for l_registro in l_registros:
        print(l_registro)

def select_all_empregado():
    sql = '''SELECT emp.idt, emp.nome, emp.data_nasc, emp.genero, car.nome
            FROM tb_empregado as emp 
            inner join tb_cargo as car 
            on emp.cod_cargo = car.idt'''
    cursor.execute(sql)
    l_registros = cursor.fetchall()
    for l_registro in l_registros:
        print("----------------")
        print(f"ID: {l_registro[0]}")
        print(f"Nome: {l_registro[1]}")
        print(f"Data de Nascimento: {l_registro[2]}")
        print(f"Genero: {l_registro[3]}")
        print(f"Cargo: {l_registro[4]}")

def delete_cargo():
    vcargodelete = input("Digite o nome do cargo a ser deletado: ")

    sql = f'''DELETE FROM tb_cargo where nome = '{vcargodelete}' '''
    print(f"Cargo {vcargodelete} foi deletado com sucesso")

    cursor.execute(sql)
    conexao.commit()

def delete_empregado():
    vempdelete = input("Digite o nome do empregado a ser deletado: ")

    sql = f'''DELETE FROM tb_empregado where nome = '{vempdelete}' '''
    print(f"Empregado {vempdelete} foi deletado com sucesso")

    cursor.execute(sql)
    conexao.commit()

def update_data():
    vnomepesq = input("Digite o nome do empregado a ter a data de nascimento atualizada: ")
    vnovadata = input("Digite a nova data: ")

    sql = f'''UPDATE tb_empregado
             set data_nasc = '{vnovadata}'
             where nome = '{vnomepesq}' '''

    cursor.execute(sql)
    conexao.commit()

def close_connection():
    cursor.close()
    conexao.close()
    print("\nConexão Fechada")

def show_records():
    sql = '''SELECT * FROM tb_cargo'''
    cursor.execute(sql)
    l_regs = cursor.fetchall()
    for l_reg in l_regs:
        print(f"ID: {l_reg[0]}")
        print(f"Nome: {l_reg[1]}")

if __name__ == "__main__":
    conexao = create_connection()
    cursor = conexao.cursor()
    create_database()
    create_table()
    while True:
        print("\n------Menu CRUD Empresa------")
        print("[1] Adicionar Cargo")
        print("[2] Adicionar Empregado")
        print("[3] Consultar tabela de Cargos")
        print("[4] Consultar Tabela de Empregados")
        print("[5] Deletar Cargo")
        print("[6] Deletar Empregado")
        print("[7] Atualizar data de nacimento de um Empregado")
        print("[8]Sair")
        print("-----------------------------")
        opc = input("\nEscolha uma das opções acima: ")

        if opc == "1":
            insert_cargo()
        elif opc == "2":
            insert_empregado()
        elif opc == "3":
            select_all_cargo()
        elif opc == "4":
            select_all_empregado()
        elif opc == "5":
            delete_cargo()
        elif opc == "6":
            delete_empregado()
        elif opc == "7":
            update_data()
        elif opc == "8":
            print("Menu encerrado com sucesso")
            break
        else:
            print("\nOpção inválida, tente novamente.")

    close_connection()