from backend.app.infrastructure.persistence.models.base import Base


from sqlalchemy.orm import mapped_column
from sqlalchemy import String, Integer, ForeignKey


class ImageModel(Base):

    """Representa uma classe mapeada com a tabela image"""

    __tablename__ = "image"

    id = mapped_column(Integer, primary_key=True)
    url = mapped_column(String(255), nullable=False)
    item_id = mapped_column(ForeignKey("item.id"))

    def __repr__(self) -> str:

        """Representa o objeto ImageModel em uma String Literal
        
        Returns
        -------
        str
            Representação do objeto em uma String Literal

        """

        return f"LocalizationModel=[{self.url}, {self.item_id}]"
    