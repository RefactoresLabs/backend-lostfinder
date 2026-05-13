from abc import ABC, abstractmethod


class GeocodeServiceInterface(ABC):

    """Interface do serviço de geocodificação"""

    @abstractmethod
    def get_coordinates(self, street: str, neighborhood: str, cep: str) -> dict | None:

        """Obtém as coordenadas geográficas a partir de dados de endereço

        Parameters
        ----------
        street: str
            Rua do endereço

        neighborhood: str
            Bairro do endereço

        cep: str
            CEP do endereço

        Returns
        -------
        dict | None
            Dicionário com latitude e longitude, ou None se não encontrado

        """
        ...
