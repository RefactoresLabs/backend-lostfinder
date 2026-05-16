from backend.app.domain.value_objects.localization import Localization


class Building:

    """Representa a entidade prédio de uma dada localização"""

    def __init__(self, id: int, name: str, associated_localization: Localization) -> None:

        """Inicializa os atributos de instância de Building

        Parameters
        ----------
        id: int
            Identificador do prédio

        name: str
            Nome do prédio
        
        associated_localization: Localization
            Localização associada ao prédio

        """

        self.__id = id
        self.__name = name
        self.__associated_localization = associated_localization
    
    @property
    def id(self) -> int:

        """Obtém o identificador do prédio

        Returns
        -------
        int
            Identificador do prédio
        
        """

        return self.__id
    
    @property
    def name(self) -> str:

        """Obtém o nome do prédio

        Returns
        -------
        str
            Nome do prédio

        """

        return self.__name
    
    @property
    def localization(self) -> Localization:

        """Obtém a localização associada ao prédio

        Returns
        -------
        Localization
            Localização associada ao prédio

        """

        return self.__associated_localization