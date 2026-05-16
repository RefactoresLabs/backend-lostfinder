from backend.app.domain.entities.found_item import FoundItem
from backend.app.domain.entities.user_account import UserAccount

from backend.app.domain.value_objects.claim_status import ClaimStatus


from datetime import datetime


class Claim:

    """Representa a entidade de negociação de recuperação de itens da regra de negócio"""

    def __init__(self, id: int | None, created_at: datetime | None, claimant_user_account: UserAccount, associated_found_item: FoundItem, status: ClaimStatus, retrieval_code: str | None=None) -> None:

        """Inicializa os atributos de instância de Claim

        Parameters
        ----------
        id: int | None
            ID da negociação
        
        created_at: datetime | None
            Data e hora que a negociação foi criada
        
        claimant_user_account: UserAccount
            Conta de usuário que criou a negociação
        
        associated_found_item: FoundItem
            Item encontrado associado a negociação
        
        status: ClaimStatus
            Status da negociação
        
        retrieval_code: str | None (Padrão: None)
            Código de recuperação associado a negociação
        
        """

        self.__id = id
        self.__created_at = created_at
        self.__claimant_user_account = claimant_user_account
        self.__associated_found_item = associated_found_item
        self.__status = status
        self.__retrieval_code = retrieval_code
    
    @property
    def id(self) -> int:

        """Obtém o ID da negociação

        Returns
        -------
        int
            ID da negociação

        """

        return self.__id
    
    @property
    def created_at(self) -> datetime:

        """Obtém a data e hora que a negociação foi criada

        Returns
        -------
        datetime
            Data e hora que a negociação foi criada
            
        """

        return self.__created_at
    
    @property
    def claimant_user_account(self) -> UserAccount:

        """Obtém a conta de usuário que criou a negociação

        Returns
        -------
        UserAccount
            Conta de usuário que criou a negociação
            
        """

        return self.__claimant_user_account
    
    @property
    def associated_found_item(self) -> FoundItem:

        """Obtém o item encontrado associado a negociação

        Returns
        -------
        FoundItem
            Item encontrado associado a negociação
            
        """

        return self.__associated_found_item
    
    @property
    def status(self) -> ClaimStatus:

        """Obtém o status da negociação

        Returns
        -------
        ClaimStatus
            Status da negociação

            
        """

        return self.__status
    
    @property
    def retrieval_code(self) -> str | None:

        """Obtém o código de recuperação da negociação

        Returns
        -------
        str | None
            Código de recuperação da negociação

        """

        return self.__retrieval_code
    
    def _set_id(self, id: int) -> None:

        """Modifica o valor do atributo id da negociação uma única vez, caso ela seja None no estado atual

        Parameters
        ----------
        id: int
            Valor a ser definido no atributo id
        
        """

        if self.__id is not None:

            raise ValueError("Valor de ID já definido!")
        
        self.__id = id
    
    def _set_created_at(self, created_at: datetime) -> None:

        """Modifica o valor do atributo created_at da negociação uma única vez, caso ela seja None no estado atual

        Parameters
        ----------
        created_at: datetime
            Valor a ser definido no atributo created_at
        
        """

        if self.__created_at is not None:

            raise ValueError("Valor da data e hora de criação já definido!")
        
        self.__created_at = created_at