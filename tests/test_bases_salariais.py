import sys
import unittest
from unittest import main,TestCase
sys.path.append(r"C:\Users\ligia\Documents\autoensino\Coding\CodeWarsII")
from src.entities.bases_salariais import INSS, IRRF
from src.entities.funcionario import Funcionario


class TestCalculoINSS(TestCase):

    def test_INSS_faixa3(self):
        funcionario = Funcionario("Ana Maria Silva", "11111111100", "2019-02-07", "32", "Sim")
        self.assertEqual((269.00, 0.12),INSS(funcionario))

    def test_IRRF_faixa3(self):
        funcionario= Funcionario("Ana Maria Silva", "11111111100", "2019-02-07", "32", "Sim")
        self.assertEqual((54.85, 0.275), IRRF(funcionario))

    def test_INSS_faixa4(self):
        funcionario= Funcionario("Ana Maria Silva", "11111111100", "2019-02-07", "20", "Sim")
        self.assertEqual((816.18, 0.14),INSS(funcionario))

    def test_IRRF_faixa4(self):
        funcionario = Funcionario("Ana Maria Silva", "11111111100", "2019-02-07", "20", "Sim")
        self.assertEqual((831.19, 0.275), IRRF(funcionario))
   
    def test_INSS_faixa5(self):
        funcionario= Funcionario("Ana Maria Silva", "11111111100", "2019-02-07", "10", "Sim")
        self.assertEqual((828.39, 0.14),INSS(funcionario))

    def test_IRRF_faixa5(self):
        funcionario = Funcionario("Ana Maria Silva", "11111111100", "2019-02-07", "10", "Sim")
        self.assertEqual((1707.83, 0.275), IRRF(funcionario))

if __name__=='__main__':
    unittest.main()