class HttpResponse:

    """Encapsula os dados da resposta HTTP"""

    def __init__(self, status_code: int, body: list[dict[str, any]] | dict[str, any] | None=None) -> None:

        """Inicializa os atributos de instância de HttpResponse

        Parameters
        ----------
        status_code: int
            Código de status da resposta HTTP

        body: list[dict[str, any]] | dict[str, any] | None (padrão: None)
            Corpo da resposta HTTP.
        
        """

        self.__status_code = status_code
        
        if isinstance(body, list):

            self.__body = list([dict(field) for field in body])
        
        elif isinstance(body, dict):

            self.__body = dict(body)
        
        else:

            self.__body = {}
    
    @property
    def status_code(self) -> int:

        """Obtém o código de status de uma resposta HTTP

        Returns
        -------
        dict[str, any]
            Corpo da resposta HTTP
            
        """

        return self.__status_code
    
    @property
    def body(self) -> list[dict[str, any]] | dict[str, any]:

        """Obtém o corpo de uma resposta HTTP

        Returns
        -------
        list[dict[str, any]] | dict[str, any]
            Corpo da resposta HTTP

        """

        return self.__body.copy()
