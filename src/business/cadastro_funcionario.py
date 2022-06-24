from msilib.schema import Error
from typing import List
from xml.dom import NotFoundErr
from src.entities.funcionario import Funcionario

class CadastroFuncionario():
    def __init__(self) -> None:
            self.__funcionarios: List[Funcionario] = []

    def incluir(self, funcionario:Funcionario):
        self.__funcionarios.append(funcionario)

    def consultar(self, matricula: str) -> Funcionario:
        entidade = list(filter(lambda x: x.matricula == matricula, self.__funcionarios))
        if entidade==[]:
            raise NotFoundErr("Matrícula não encontrada.")
        else:
            return entidade

    def excluir(self, matricula: str) -> None:
        entidade = self.consultar(matricula)
        self.__funcionarios.remove(entidade)

    def alterar_cadastro(self, matricula: str) -> None:
        entidade = self.consultar(matricula)
        self.__funcionarios.remove(entidade)
        self.__funcionarios.incluir(entidade)

    def listar_todos(self) -> List[Funcionario]:
        return self.__funcionarios
