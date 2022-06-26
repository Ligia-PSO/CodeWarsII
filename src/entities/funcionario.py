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