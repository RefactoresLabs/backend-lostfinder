from abc import ABC, abstractmethod


class TokenGenerator(ABC):

    """Interface para geração de tokens de autenticação"""

    @abstractmethod
    def generate(self, payload: dict) -> str:

        """Gera um token a partir de um payload

        Parameters
        ----------
        payload: dict
            Dados a serem embutidos no token

        Returns
        -------
        str
            Token gerado

        """
