from src.entities.bases_salariais import INSS, IRRF
from src.business.cadastro_funcionario import CadastroFuncionario
from src.entities.funcionario import Funcionario

class Holerite():
    def __init__(self, cpf: str, mes: int, faltas: int=0):
        self.__mes_referencia = mes
        self.__cpf = cpf
        self.__faltas = faltas

        # -----------Gerado consultando base de dados e por calculo----------
        self.__comissao: float = self.funcionario().cargo().comissao
        self.__salario_base: float = self.funcionario().cargo().salario_base
        # self.__inss = INSS(self.funcionario())[0]
        # self.__irrf = IRRF(self.funcionario())[0]

    def funcionario(self) -> Funcionario:
        cadastro = CadastroFuncionario()
        funcionario = cadastro.consultar(self.cpf)
        return funcionario

    @property
    def mes_referencia(self) -> int:
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
    def cpf(self) -> float:
        return self.__cpf
