from backend.app.infrastructure.persistence.models.base import Base

from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String

class UserAccountModel(Base):

    """Representa uma classe mapeada com a tabela user_account"""

    __tablename__ = "user_account"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(255), nullable=False)
    email = mapped_column(String(255), nullable=False, unique=True)
    password = mapped_column(String(255), nullable=False)
    phone = mapped_column(String(20), nullable=False)

    def __repr__(self) -> str:

        """Representa o objeto UserAccountModel em uma String Literal
        
        Returns
        -------
        str
            Representação do objeto em uma String Literal

        """

        return f"UserAccount=[{self.id}, {self.name}, {self.email}]"

