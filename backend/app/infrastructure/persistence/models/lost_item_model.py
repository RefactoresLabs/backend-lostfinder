from backend.app.infrastructure.persistence.models.base import Base


from sqlalchemy.orm import mapped_column
from sqlalchemy import ForeignKey


class LostItemModel(Base):

    """Representa uma classe mapeada com a tabela lost_item"""

    __tablename__ = "lost_item"

    id = mapped_column(ForeignKey("item.id"), primary_key=True)
    lost_space_id = mapped_column(ForeignKey("building_space.id"))


    def __repr__(self) -> str:

        """Representa o objeto LostItemModel em uma String Literal
        
        Returns
        -------
        str
            Representação do objeto em uma String Literal

        """

        return f"LostItemModel=[{self.id}, {self.lost_space_id}]"