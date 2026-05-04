from abc import ABC, abstractmethod

class PasswordHasher(ABC):

    """Interface para um algoritmo de hash aplicado a senha da conta de usuário"""

    @abstractmethod
    def hash(self, password: str) -> str: ...

    @abstractmethod
    def verify(self, password: str, hashed_password: str) -> str: ...

    