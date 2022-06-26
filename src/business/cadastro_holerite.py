import mysql.connector

class CadastroHolerite():

    def todos_holerites(self):

        pass

    def gerar_holerite(self,cpf:str):
        cnx = mysql.connector.connect(user='root', password='throwaway11',
                              host='127.0.0.1',
                              database='xpto_alimentos')
                              
        cursor = cnx.cursor()

        mes=input('informe o mes do holerite(em numero)')
        # data=
        faltas=int(input('quantas faltas?'))

        
        pass