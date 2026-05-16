from backend.app.infrastructure.persistence.models.base import Base


from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey


class FoundItemModel(Base):

    """Representa uma classe mapeada com a tabela found_item"""

    __tablename__ = "found_item"

    id = mapped_column(ForeignKey("item.id"), primary_key=True)
    found_space_id = mapped_column(ForeignKey("building_space.id"))
    left_space_id = mapped_column(ForeignKey("building_space.id"))


    def __repr__(self) -> str:

        """Representa o objeto FoundItemModel em uma String Literal
        
        Returns
        -------
        str
            Representação do objeto em uma String Literal

        """

        return f"FoundItemModel=[{self.id}, {self.found_space_id}, {self.left_space_id}]"