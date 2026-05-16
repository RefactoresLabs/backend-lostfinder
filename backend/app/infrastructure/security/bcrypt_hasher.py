import bcrypt

from backend.app.application.interfaces.password_hasher import PasswordHasher

class BcryptHasher(PasswordHasher):

    """Algoritmo de hash bcrypt para hash da senha da conta de usuário"""

    def hash(self, password: str) -> str:

        """Gera o hash da mensagem com o algoritmo bcrypt

        Parameters
        ----------
        message: str
            Mensagem a ser cifrada
        
        Returns
        -------
        str
            Hash da senha em hexadecimal

        """

        hashed_password = bcrypt.hashpw(
            password.encode("utf-8"),
            bcrypt.gensalt(14)
        ).decode("utf-8")

        return hashed_password
    
    def verify(self, password: str, hashed_password: str) -> bool:

        """Verifica se hashed_password corresponde a password quando aplicado o bcrypt

        Parameters
        ----------
        password: str
            Senha que será verificada a correspondência
        
        hashed_password:
            Hash da senha que será verificada a correspondência
        
        Returns
        -------
        bool
            True se corresponderem, False caso contrário

        """
        
        return bcrypt.checkpw(
            password.encode("utf-8"),
            hashed_password.encode("utf-8")
        )

    