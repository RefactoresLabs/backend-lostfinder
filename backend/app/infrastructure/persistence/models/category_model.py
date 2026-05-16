from backend.app.infrastructure.persistence.models.base import Base


from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String


class CategoryModel(Base):

    """Representa uma classe mapeada com a tabela category"""

    __tablename__ = "category"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(255), nullable=False)

    def __repr__(self) -> str:

        """Representa o objeto CategoryModel em uma String Literal
        
        Returns
        -------
        str
            Representação do objeto em uma String Literal

        """

        return f"Category=[{self.id}, {self.name}]"