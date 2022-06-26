import mysql.connector
import sys
sys.path.append(r"C:\Users\ligia\Documents\autoensino\Coding\CodeWarsII")
from mysql.connector.errors import IntegrityError,DatabaseError
from src.entities.bases_salariais import INSS, IRRF
from src.entities.holerites import Holerite
from src.business.cadastro_funcionario import CadastroFuncionario

from src.entities.funcionario import Funcionario

class CadastroHolerite():

    def todos_holerites(self):

        pass

    def gerar_holerite(self,cpf:str):
        cnx = mysql.connector.connect(user='root', password='throwaway11',
                              host='127.0.0.1',
                              database='xpto_alimentos')
                              
        cursor = cnx.cursor()
        query = ('''SELECT matricula FROM funcionario WHERE CPF=%s''')
        cursor.execute(query, [cpf])

        funcionario=CadastroFuncionario().consultar(cpf)

        mes_referencia=input('informe o mes do holerite(em numero)')
        faltas=int(input('quantas faltas?'))
        
        holerite=Holerite(cpf,mes_referencia,faltas)

        adiciona_holerite = (
            """INSERT INTO holerite
            (funcionario_CPF,mes,faltas) 
            VALUES ( %(funcionario_CPF)s, %(mes)s, %(faltas)s)"""
        )

        dados = {
            "funcionario_CPF": holerite.cpf,
            "mes": holerite.mes_referencia,
            "faltas": holerite.faltas,
        }

        try:
            cursor.execute(adiciona_holerite, dados)
            cnx.commit()
        except IntegrityError:
            print(f'O funcionario {funcionario.nome} ja tem as faltas no mes {mes_referencia} registradas')
            cursor.close()
            cnx.close()
            exit()
        except DatabaseError:
            print(f"mes {mes_referencia} nao é valido")
            cursor.close()
            cnx.close()
            exit()

# =================Print Holerite==========================      
        salario_base=funcionario.cargo().salario_base
        comissao=funcionario.cargo().comissao*100
        
        inss,aliquota_inss=INSS(funcionario)
        irrf,aliquota_irrf=IRRF(funcionario)

        [(matricula,)]=cursor.fetchall()

        print("    ".join(['   Matricula   ', 'Nome         ',
              'CPF', "Data de admissao", "Cargo id ", "Comissao"]))
       
        print(matricula,funcionario.nome,funcionario.CPF,funcionario.data_admissao,funcionario.cargo().descricao,funcionario.cargo().comissao)
        print('Descrição    Referencia  Provento   Desconto')
        print('Salário Base','22,5',salario_base,'   ')
        print('Comissão',comissao,comissao)
        print('Faltas', faltas, '    ', funcionario.cargo().salario_base/30*faltas)
        print('INSS Folha', aliquota_inss,'    ', inss)
        print('IRRF Folha', aliquota_irrf,'    ', irrf)

        cursor.close()
        cnx.close()
        
        pass


