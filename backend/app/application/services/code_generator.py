import string
import secrets


class CodeGenerator:

    """Algoritmo responsável por gerar um código de recuperação aleatório para a negociação"""

    @staticmethod
    def generate(length: int=10) -> str:

        """Gera um código de recuperação aleatório

        Parameters
        ----------
        length: int (Padrão: 10)
            Tamanho do código
        
        Returns
        -------
        str
            Código de recuperação aleatório

        """

        possible_chars = string.ascii_uppercase + string.digits

        return "".join([
            secrets.choice(possible_chars)
            for _ in range(length)
        ])