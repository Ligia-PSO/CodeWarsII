from src.entities.funcionario import Funcionario
from xml.dom import NotFoundErr
import mysql.connector
import sys
sys.path.append(r"C:\Users\ligia\Documents\autoensino\Coding\CodeWarsII")


class CadastroFuncionario():

    def __init__(self):
        self.__campos: list = ['nome', 'CPF',
                               'data_admissao', 'cargo_id', 'comissao']

    def inserir(self, funcionario: Funcionario):
        cnx = mysql.connector.connect(user='root', password='throwaway11',
                                      host='127.0.0.1',
                                      database='xpto_alimentos')

        cursor = cnx.cursor()

        adiciona_funcionario = (
            """INSERT INTO funcionario
            (nome,CPF,data_admissao,cargo_id,comissao ) 
            VALUES ( %(nome)s, %(CPF)s, %(data_admissao)s, %(cargo_id)s, %(comissao)s)"""
        )

        dados = {
            "nome": funcionario.nome,
            "CPF": funcionario.CPF,
            "data_admissao": funcionario.data_admissao,
            "cargo_id": funcionario.cargo_id,
            "comissao": funcionario.comissao
        }

        cursor.execute(adiciona_funcionario, dados)

        cnx.commit()
        cursor.close()
        cnx.close()

    def consultar(self, cpf: str) -> Funcionario:
        cnx = mysql.connector.connect(user='root', password='throwaway11',
                                      host='127.0.0.1',
                                      database='xpto_alimentos')

        cursor = cnx.cursor()

        query = (
            '''SELECT nome, CPF, data_admissao, cargo_id, comissao 
        FROM funcionario 
        WHERE CPF=%s'''
        )

        cursor.execute(query, [cpf])

        for (nome, cpf, data_admissao, cargo_id, comissao) in cursor:
            funcionario = Funcionario(
                nome, cpf, data_admissao, cargo_id, comissao)

        cursor.close()
        cnx.close()

        return funcionario

    def excluir(self, cpf: str) -> None:
        cnx = mysql.connector.connect(user='root', password='throwaway11',
                                      host='127.0.0.1',
                                      database='xpto_alimentos')
        cursor = cnx.cursor()

        deleta_funcionario = (
            '''DELETE FROM funcionario 
        WHERE CPF = %s'''
        )

        cursor.execute(deleta_funcionario, (cpf,))

        cnx.commit()
        cursor.close()
        cnx.close()

    def alterar_cadastro(self, cpf: str) -> None:
        cnx = mysql.connector.connect(user='root', password='throwaway11',
                                      host='127.0.0.1',
                                      database='xpto_alimentos')
        cursor = cnx.cursor()

        # Listagem de cpf no database
        cursor.execute('''SELECT CPF 
        FROM xpto_alimentos.funcionario''')
        cpf_list = list(map(lambda x: x[0], cursor.fetchall()))

        if cpf in cpf_list:
            for i in range(len(self.__campos)):
                print(f"{i}----{self.__campos[i]}")

            index = int(input('Informe o codigo do campo a ser alterado:'))

            if index not in range(len(self.__campos)):
                print('codigo de campo nao existe')
            else:
                alteraçao = input('Nova info:\n')

            if alteraçao == None or alteraçao.isspace() or alteraçao == '':
                print('novo dado nao pode ser vazio')
            else:
                if "s" == input(f'Deseja alterar {self.__campos[index]} para "{alteraçao}"?(s/n) '):
                    sql = "UPDATE funcionario SET " + \
                        self.__campos[index]+" = %s WHERE CPF = %s"
                    cursor.execute(sql, (alteraçao, cpf))
                    cnx.commit()
                    print("alteracao feita")
        else:
            # fazer um erro customizado de cpfnotfound(excecao)
            raise NotFoundErr

        cursor.close()
        cnx.close()

    def listar_todos(self) -> list:

        cnx = mysql.connector.connect(user='root', password='throwaway11',
                                      host='127.0.0.1',
                                      database='xpto_alimentos')
        cursor = cnx.cursor()

        lista_funcionarios = (
            '''SELECT * 
        FROM xpto_alimentos.funcionario'''
        )

        # criar erro se nao ha funcionarios cadastrados(excecao)

        cursor.execute(lista_funcionarios)

        aux = cursor.fetchall()

        print("    ".join(['   Matricula   ', 'Nome         ',
              'CPF', "Data de admissao", "Cargo id ", "Comissao"]))

        for i in range(len(aux)):
            print("  ", "    ".join(map(str, aux[i])))

        cursor.close()
        cnx.close()
        return aux
