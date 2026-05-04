from backend.app.domain.entities.building import Building


class BuildingSpace:

    """Representa a entidade espaço de um prédio"""

    def __init__(self, id: int, name: str, associated_building: Building) -> None:

        """Inicializa os atributos de instância de BuildingSpace

        Parameters
        ----------
        id: int
            Identificador do espaço do prédio

        name: str
            Nome do espaço do prédio
        
        associated_building: Building
            Prédio que o espaço está associado

        """

        self.__id = id
        self.__name = name
        self.__associated_building = associated_building
    
    @property
    def id(self) -> int:

        """Obtém o identificador do espaço do prédio

        Returns
        -------
        int
            Identificador do espaço do prédio
        
        """

        return self.__id
    
    @property
    def name(self) -> str:

        """Obtém o nome do espaço do prédio

        Returns
        ----------
        str
            Nome do espaço do prédio

        """

        return self.__name
    
    @property
    def associated_building(self) -> Building:

        """Obtém o prédio associado ao espaço

        Returns
        -------
        Building
            Prédio associado ao espaço

        """

        return self.__associated_building