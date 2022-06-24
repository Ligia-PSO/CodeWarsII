import sys
import pytest
sys.path.insert(1, r'C:\Users\ligia\Documents\autoensino\Coding\codigo[s]\aulas\CodeWars2')

from src.entities.funcionario import Funcionario
from src.business.cadastro_funcionario import CadastroFuncionario

funcionario1=Funcionario('21840915751','Julios','1234455677','10/09/2010',True)
funcionario2=Funcionario('74545345384','Amanda','4548548548','12/10/2012',True)

print(funcionario1.nome)

cadastro=CadastroFuncionario()
cadastro.incluir(funcionario2)
print(cadastro.listar_todos())

@pytest.fixture()
def setup():
    cadastro=CadastroFuncionario()

    funcionario1=Funcionario('21840915751','Julios','1234455677','10/09/2010',True)
    funcionario2=Funcionario('74545345384','Amanda','4548548548','12/10/2012',True)


    pass

def test_incluir_cliente():
    pass


