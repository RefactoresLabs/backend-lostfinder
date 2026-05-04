from backend.app.infrastructure.persistence.models.base import Base


from sqlalchemy.orm import mapped_column
from sqlalchemy import String, Integer, ForeignKey


class BuildingModel(Base):

    """Representa uma classe mapeada com a tabela building"""

    __tablename__ = "building"

    id = mapped_column(Integer, primary_key=True)
    name = mapped_column(String(255), nullable=False)
    localization_id = mapped_column(ForeignKey("localization.id"))
    
    def __repr__(self) -> str:

        """Representa o objeto BuildingModel em uma String Literal
        
        Returns
        -------
        str
            Representação do objeto em uma String Literal

        """

        return f"BuildingModel=[{self.id}, {self.name}]"