from sqlalchemy.orm import Session
from typing import Any

from backend.app.infrastructure.persistence.models.claim_model import ClaimModel
from backend.app.infrastructure.persistence.models.found_item_model import FoundItemModel
from backend.app.infrastructure.persistence.models.item_model import ItemModel
from backend.app.infrastructure.persistence.models.user_account_model import UserAccountModel

from backend.app.application.interfaces.claim_query_service_interface import ClaimQueryServiceInterface


class ClaimQueryService(ClaimQueryServiceInterface):

    """Lida com transações mais específicas de negociações de recuperação de item"""

    def __init__(self, session: Session) -> None:

        """Inicializa os atributos de instância de ClaimQueryService

        Parameters
        ----------
        session: Session
            Sessão que lida com transações

        """

        self.__session = session

    def get_created_claims_summarized_by_user_id(self, user_id: int) -> list[dict[str, Any]]:

        """Obtém os dados resumidos das negociações criadas por uma conta de usuário

        Retorna somente os campos necessários para o endpoint my-created-claims:
        id da negociação, nome do claimant e id + nome do item encontrado associado.

        Parameters
        ----------
        user_id: int
            ID da conta de usuário que criou as negociações

        Returns
        -------
        list[dict[str, Any]]
            Iterável com dados resumidos das negociações criadas pelo usuário

        """

        ClaimantUser = UserAccountModel

        results = (
            self.__session.query(
                ClaimModel.id,
                ClaimantUser.name,
                ItemModel.id,
                ItemModel.name,
            )
            .join(
                ClaimantUser,
                ClaimantUser.id == ClaimModel.claimant_user_account_id,
            )
            .join(
                FoundItemModel,
                FoundItemModel.id == ClaimModel.associated_found_item_id,
            )
            .join(
                ItemModel,
                ItemModel.id == FoundItemModel.id,
            )
            .filter(
                ClaimModel.claimant_user_account_id == user_id,
            )
            .all()
        )

        return [
            {
                "claim_id": result[0],
                "claimant_user_name": result[1],
                "found_item_id": result[2],
                "found_item_name": result[3],
            }
            for result in results
        ]

    def get_received_claims_summarized_by_user_id(self, user_id: int) -> list[dict[str, Any]]:

        """Obtém os dados resumidos das negociações recebidas por uma conta de usuário

        Retorna somente os campos necessários para o endpoint my-received-claims:
        id da negociação, id + nome do item encontrado e nome do dono do item encontrado.

        Parameters
        ----------
        user_id: int
            ID da conta de usuário que é dona dos itens encontrados das negociações

        Returns
        -------
        list[dict[str, Any]]
            Iterável com dados resumidos das negociações recebidas pelo usuário

        """

        # Alias para distinguir o dono do found_item do claimant
        FoundItemOwner = UserAccountModel

        results = (
            self.__session.query(
                ClaimModel.id,
                ItemModel.id,
                ItemModel.name,
                FoundItemOwner.name,
            )
            .join(
                FoundItemModel,
                FoundItemModel.id == ClaimModel.associated_found_item_id,
            )
            .join(
                ItemModel,
                ItemModel.id == FoundItemModel.id,
            )
            .join(
                FoundItemOwner,
                FoundItemOwner.id == ItemModel.user_id,
            )
            .filter(
                ItemModel.user_id == user_id,
            )
            .all()
        )

        return [
            {
                "claim_id": result[0],
                "found_item_id": result[1],
                "found_item_name": result[2],
                "found_item_owner_name": result[3],
            }
            for result in results
        ]