from src.exception.base_funcionario_error import BaseFuncionarioError


class NotFoundError(BaseFuncionarioError):

    def __init__(self, *args: object) -> None:
        super().__init__(*args)

# class 