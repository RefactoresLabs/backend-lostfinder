from backend.app.infrastructure.persistence.models.base import Base


from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String


class ClaimStatusModel(Base):

    """Representa uma classe mapeada com a tabela claim_status"""

    __tablename__ = "claim_status"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(255), nullable=False)

    def __repr__(self) -> str:

        """Representa o objeto ClaimStatusModel em uma String Literal
        
        Returns
        -------
        str
            Representação do objeto em uma String Literal

        """

        return f"ClaimStatusModel=[{self.id}, {self.name}]"