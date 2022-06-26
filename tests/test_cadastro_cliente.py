
import sys
sys.path.append()
sys.path.append(r"C:\Users\ligia\Documents\autoensino\Coding\CodeWarsII")
from src.entities.funcionario import Funcionario
from src.business.cadastro_funcionario import CadastroFuncionario

#precisa ser mudado para iplementação do pytest ou unittest

cadastro = CadastroFuncionario()

funcionario = Funcionario('Ana Maria Silva', '11111111122', '2019-02-07', '32', 'Sim')

# ----------------------TEST  inserir-----------------OK
# cadastro.inserir(funcionario)

# ----------------------TEST  consultar--------------- OK

# cadastro.consultar("11111111122")

# ----------------------TEST  excluir-----------------OK
# cadastro.excluir("11111111122")

# ----------------------TEST  alterar-----------------
# cadastro.alterar_cadastro("11111111122")

# ----------------------TEST  listar-----------------OK
cadastro.listar_todos()