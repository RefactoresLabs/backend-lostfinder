class PasswordsDontMatchError(Exception):

    """Representa o erro de senhas que não correspondem no registro"""

    def __init__(self) -> None:

        """Inicializa a exceção com uma mensagem padrão"""

        super().__init__("Senha e confirmar senha não correspondem")
