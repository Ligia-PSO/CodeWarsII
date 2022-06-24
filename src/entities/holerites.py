class Holerites():
    def __init__(self, mes_referencia: str, salario_base: float, comissao: float, faltas: int, INSS_folha: float, IRRF_folha: float):
        self.__mes_referencia: float = mes_referencia
        self.__salario_base: float = salario_base
        self.__comissao: float = comissao
        self.__faltas: int = faltas
        self.__INSS_folha: float = INSS_folha
        self.__IRRF_folha: float = IRRF_folha

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
    def INSS_folha(self) -> float:
        return self.__INSS_folha
    
    @property
    def IRRF_folha(self) -> float:
        return self.__IRRF_folha