class Funcionario():
    def __init__(self, matricula: str, nome: str, CPF: str, data_admissao: str, comissao: bool)->None:
        self.__matricula: str = matricula
        self.__nome: str = nome
        self.__CPF: str = CPF
        self.__data_admissao: str = data_admissao
        self.__comissao: bool = comissao

    @property
    def nome(self) -> str:
        return self.__nome

    @property
    def CPF(self) -> int:
        return self.__CPF

    @property
    def data_admissao(self) -> str:
        return self.__data_admissao
    
    @property
    def comissao(self) -> float:
        return self.__comissao
