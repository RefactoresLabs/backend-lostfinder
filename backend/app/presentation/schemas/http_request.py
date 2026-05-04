class HttpRequest:

    """Encapsula os dados da requisição HTTP"""

    def __init__(self, params: dict[str, any] | None=None, body: dict[str, any] | None=None) -> None:

        """Inicializa os atributos de instância de HttpResquest

        Parameters
        ----------
        params: dict[str, any] (padrão: None)
            Parâmetros da requisição HTTP.
        
        body: dict[str, any] (padrão: None)
            Corpo da requisição HTTP.
        
        """

        self.__params = dict(params) if params else {}
        self.__body = dict(body) if body else {}
    
    @property
    def params(self) -> dict[str, any] :

        """Obtém os parâmetros de uma requisição HTTP

        Returns
        -------
        dict[str, any]
            Parâmetros da requisição HTTP

        """

        return self.__params.copy()

    @property
    def body(self) -> dict[str, any] :

        """Obtém o corpo de uma requisição HTTP

        Returns
        -------
        dict[str, any]
            Corpo da requisição HTTP
            
        """

        return self.__body.copy()
