from backend.app.infrastructure.persistence.models.base import Base


from datetime import date


from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, String, Text, ForeignKey, Date


class ItemModel(Base):

    """Representa uma classe mapeada com a tabela item"""

    __tablename__ = "item"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(255), nullable=False)
    description = mapped_column(Text)
    registration_date = mapped_column(Date, default=date.today)
    category_id = mapped_column(ForeignKey("category.id"))
    user_id = mapped_column(ForeignKey("user_account.id"))
    

    def __repr__(self) -> str:

        """Representa o objeto ItemModel em uma String Literal
        
        Returns
        -------
        str
            Representação do objeto em uma String Literal

        """

        return f"ItemModel=[{self.id}, {self.name}]"