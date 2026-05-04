from backend.app.infrastructure.persistence.models.base import Base


from sqlalchemy.orm import mapped_column
from sqlalchemy import String, Integer


class LocalizationModel(Base):

    """Representa uma classe mapeada com a tabela localization"""

    __tablename__ = "localization"

    id = mapped_column(Integer, primary_key=True)
    cep = mapped_column(String(255), nullable=False)
    neighborhood = mapped_column(String(255), nullable=False)
    street = mapped_column(String(255), nullable=False)

    def __repr__(self) -> str:

        """Representa o objeto LocalizationModel em uma String Literal
        
        Returns
        -------
        str
            Representação do objeto em uma String Literal

        """

        return f"LocalizationModel=[{self.cep}, {self.neighborhood}, {self.street}]"
    