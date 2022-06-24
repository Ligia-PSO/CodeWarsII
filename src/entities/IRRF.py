class IRRF():
    def calcula(self):
        pass

    # DOIS UNDERLINES!
    def _str_(self):
        return "Print da classe imposto"

    def _repr_(self):
        return "Representação da classe imposto"
    # salario_irrf = Funcionario.salario_base + Cargo.comissao(salario_base) - INSS(salario_base)
class Faixa_1(IRRF):
    def calcula(self, salario_base):
        return salario_base * (0.075)
