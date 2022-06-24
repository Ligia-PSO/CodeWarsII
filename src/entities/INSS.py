class INSS():
    def calcula(self):
        pass

    # DOIS UNDERLINES!
    def _str_(self):
        return "Print da classe imposto"

    def _repr_(self):
        return "Representação da classe imposto"

class Faixa_1(INSS):
    def calcula(self, salario_base):
        return salario_base * (0.075)

class Faixa_2(INSS):
    def calcula(self, salario_base):
        return 1212 * 0.075 + (salario_base - 1212) * 0.09

class Faixa_3(INSS):
    def calcula(self, salario_base):
        return (1212 * 0.075 + (2427.35 - 1212) *
         0.09 + (salario_base - 2427.35) * 0.12)

class Faixa_4(INSS):
    def calcula(self, salario_base):
        return (1212 * 0.075 + (2427.35 - 1212) * 0.09 + (3641.04 - 2427.35)
         * 0.12 + (salario_base - 3641.04) * 0.14)

##conferir validade (acima do teto estipulado)
class Faixa_4_especial(INSS):
    def calcula(self, salario_base):
        return (1212 * 0.075 + (2427.35 - 1212) * 0.09 + (3641.04 - 2427.35)
         * 0.12 + (salario_base - 3641.04) * 0.14)