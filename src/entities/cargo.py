class Cargo():
    def __init__(self, codigo: str, descricao: str, salario_base: float, comissao: float):
        self.__codigo: str = codigo
        self.__descricao: str = descricao
        self.__salario_base: str = salario_base
        self.__comissao: str = comissao
        
    
    @property
    def codigo(self) -> str:
        return self.__codigo
    
    @property
    def descricao(self) -> str:
        return self.__descricao    
    
    @property
    def salario_base(self) -> float:
        return self.__salario_base   

    @property
    def comissao(self) -> float:
        return self.__comissao