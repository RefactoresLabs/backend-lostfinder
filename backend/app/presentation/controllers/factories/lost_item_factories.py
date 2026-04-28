from backend.app.application.use_cases.list_lost_items_summarized_use_case import ListLostItemsSummarizedUseCase

from backend.app.infrastructure.queries.lost_item_query_service import LostItemQueryService

from backend.app.presentation.controllers.list_lost_items_summarized_controller import ListLostItemsSummarizedController


from sqlalchemy.orm import Session


def make_list_lost_item_summarized_controller(session: Session):

    """Factory function que cria um objeto ListLostItemsSummarizedController

    Parameters
    ----------
    session: Session
        Sessão usada para as transações com o banco
    
    Returns
    -------
    ListLostItemsSummarizedController
        Ponto de acesso do endpoint com o caso de uso de listar itens perdidos resumidamente
        
    """

    query_service = LostItemQueryService(session)

    use_case = ListLostItemsSummarizedUseCase(query_service)

    return ListLostItemsSummarizedController(use_case)



    