from src.entities.cargo import Cargo
import mysql.connector

class Funcionario():
    def __init__(self, nome: str, CPF: str, data_admissao: str, cargo_id: str,comissao: str)->None:
        self.__nome: str = nome
        self.__CPF: str = CPF
        self.__data_admissao: str = data_admissao
        self.__comissao: str = comissao
        self.__cargo_id: str=cargo_id

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def CPF(self) -> str:
        return self.__CPF

    @property
    def data_admissao(self) -> str:
        return self.__data_admissao
    
    @property
    def comissao(self) -> str:
        return self.__comissao

    @property
    def cargo_id(self) -> str:
        return self.__cargo_id

    def cargo(self)->Cargo:
        '''
        Retorna a classe cargo associada ao id de dargo do funcionario
        '''
        cnx = mysql.connector.connect(user='root', password='throwaway11',
                              host='127.0.0.1',
                              database='xpto_alimentos')
                              
        cursor = cnx.cursor()

        query = (
        '''SELECT id,descricao,salario_base, comissao 
        FROM cargo 
        WHERE id=%s'''
        )

        cursor.execute(query, [self.cargo_id])
        for (codigo, descricao, salario_base, comissao) in cursor:
            cargo = Cargo(codigo, descricao, salario_base, comissao)
            
        cursor.close()
        cnx.close()
        return cargo

