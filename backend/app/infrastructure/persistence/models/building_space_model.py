from backend.app.infrastructure.persistence.models.base import Base


from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String, ForeignKey


class BuildingSpaceModel(Base):

    """Representa uma classe mapeada com a tabela building_space"""

    __tablename__ = "building_space"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(255), nullable=False)
    building_id = mapped_column(ForeignKey("building.id"))

    def __repr__(self) -> str:

        """Representa o objeto BuildingSpaceModel em uma String Literal
        
        Returns
        -------
        str
            Representação do objeto em uma String Literal

        """

        return f"BuildingSpaceModel=[{self.id}, {self.name}]"