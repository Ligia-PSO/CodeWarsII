from src.entities.bases_salariais import INSS, IRRF
from src.business.cadastro_funcionario import CadastroFuncionario
from src.entities.funcionario import Funcionario

class Holerites():
    def __init__(self, cpf: str, mes: str, faltas: int):
        self.__mes_referencia = mes
        self.__cpf = cpf
        self.__faltas = faltas

        # -----------Gerado consultando base de dados e por calculo----------
        self.__comissao: float = self.funcionario().cargo().comissao
        self.__salario_base: float = self.funcionario().cargo().salario_base
        self.__inss = INSS(self.funcionario())
        self.__irrf = IRRF(self.funcionario())

    def funcionario(self) -> Funcionario:
        cadastro = CadastroFuncionario()
        funcionario = cadastro.consultar(self.cpf)
        return funcionario

    @property
    def mes_referencia(self) -> str:
        return self.__mes_referencia

    @property
    def salario_base(self) -> float:
        return self.__salario_base

    @property
    def comissao(self) -> float:
        return self.__comissao

    @property
    def faltas(self) -> int:
        return self.__faltas

    @property
    def inss(self) -> float:
        return self.__inss

    @property
    def irrf(self) -> float:
        return self.__irrf

    @property
    def cpf(self) -> float:
        return self.__cpf
