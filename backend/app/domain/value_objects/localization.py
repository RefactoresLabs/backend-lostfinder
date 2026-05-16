class Localization:

    """Representa uma localização"""

    def __init__(self, cep: str, neighborhood: str, street: str) -> None:

        """Inicializa os atributos de instância de Localization

        Parameters
        ----------
        cep: str
            CEP referente a localização
        
        neighborhood: str
            Bairro referente a localização
        
        street: str
            Rua referente a localização

        """

        self.__cep = cep
        self.__neighborhood = neighborhood
        self.__street = street
    
    @property
    def cep(self) -> str:

        """Obtém o CEP da localização

        Returns
        -------
        str
            CEP da localização

        """

        return self.__cep

    @property
    def neighborhood(self) -> str:

        """Obtém o bairro da localização

        Returns
        -------
        str
            Bairro da localização

        """

        return self.__neighborhood
    
    @property
    def street(self) -> str:

        """Obtém a rua da localização

        Returns
        -------
        str
            Rua da localização

        """

        return self.__street