import sys
sys.path.append(r"C:\Users\ligia\Documents\autoensino\Coding\CodeWarsII")
from src.entities.funcionario import Funcionario
from src.business.cadastro_funcionario import CadastroFuncionario
# from src.entities.holerites import Holerites
from src.business.cadastro_holerite import CadastroHolerite

#precisa ser mudado para iplementação do pytest ou unittest

cadastro = CadastroFuncionario()
cadastro_holerite=CadastroHolerite()

funcionario = Funcionario('dadasdasd', '11111311122', '2019-02-07', '32', 'Sim')
# print(funcionario.matricula)
# holerite=Holerite('22222222200','2',1)
# cadastro.inserir(funcionario)

cadastro_holerite.gerar_holerite('11111111100')

# cadastro_holerite.todos_holerites()

# print(holerite.inss)#funcionando
# print(holerite.irrf)#funcionando
# print(funcionario.cargo().salario_base)#funcionando

# ----------------------TEST  inserir-----------------OK
# cadastro.inserir(funcionario)

# ----------------------TEST  consultar--------------- OK

# print(cadastro.consultar('11111111122').matricula)

# ----------------------TEST  excluir-----------------OK
# cadastro.excluir("22222222200")

# ----------------------TEST  alterar-----------------
# cadastro.alterar_cadastro("11111111122")

# ----------------------TEST  listar-----------------OK
# cadastro.listar_todos()