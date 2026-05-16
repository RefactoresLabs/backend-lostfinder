class InvalidCredentialsError(Exception):

    """Representa o erro de credenciais inválidas ao tentar autenticar"""

    def __init__(self) -> None:

        """Inicializa a exceção com uma mensagem padrão"""

        super().__init__("Credenciais inválidas")
