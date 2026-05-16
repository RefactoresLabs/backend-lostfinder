from backend.app.infrastructure.persistence.models.base import Base


from sqlalchemy.orm import mapped_column
from sqlalchemy import Integer, DateTime, String, ForeignKey


from datetime import datetime


class ClaimModel(Base):

    """Representa uma classe mapeada com a tabela claim"""

    __tablename__ = "claim"

    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    created_at = mapped_column(DateTime, nullable=False, default=datetime.now)
    retrieval_code = mapped_column(String(10), default=None, nullable=True)
    claimant_user_account_id = mapped_column(ForeignKey("user_account.id"))
    associated_found_item_id = mapped_column(ForeignKey("found_item.id"))
    status_id = mapped_column(ForeignKey("claim_status.id"))

    def __repr__(self) -> str:

        """Representa o objeto ClaimModel em uma String Literal
        
        Returns
        -------
        str
            Representação do objeto em uma String Literal

        """

        return f"ClaimModel=[{self.id}, {self.created_at}]"