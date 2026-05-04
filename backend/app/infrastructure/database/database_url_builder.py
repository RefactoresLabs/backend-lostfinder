class DatabaseURLBuilder:

    """Lida com a construção da URL do banco de dados usado pela engine de SessionManager"""

    @staticmethod
    def build(driver: str, data: dict[str, str]) -> str:

        """Constroí a url

        Parameters
        ----------
        driver: str
            Driver do SGBD
        
        data: dict[str, str]
            Dados de autenticação do banco gerenciado pelo SGBD
        
        Returns
        -------
        str
            URL do banco de dados construída

        """

        if driver.startswith("sqlite"):

            database = data.get("DATABASE", ":memory:")

            if not isinstance(database, str):

                raise TypeError("O campo DATABASE precisa ser string")
            
            return f"{driver}:///{database}"
        
        required_fields = [
            "USERNAME", 
            "PASSWORD", 
            "HOSTNAME", 
            "PORT", 
            "DATABASE"
        ]

        for field in required_fields:

            if not isinstance(data[field], str):

                raise TypeError(f"O valor de {field} precisa ser String!")
        
        user = data["USERNAME"]
        password = data["PASSWORD"]
        host = data["HOSTNAME"]
        port = data["PORT"]
        database = data["DATABASE"]

        return f"{driver}://{user}:{password}@{host}:{port}/{database}"