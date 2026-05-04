class Image:

    """Representa uma imagem associada a um item"""

    def __init__(self, url: str) -> None:

        """Inicializa os atributos de instância de Image

        Parameters
        ----------

        url: str
            URL da imagem

        """

        self.__url = url
    
    @property
    def url(self) -> str:

        """Obtém a url da imagem

        Returns
        -------
        str
            URL da imagem
        """

        return self.__url