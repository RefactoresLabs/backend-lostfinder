import requests

from backend.app.application.interfaces.geocode_service_interface import GeocodeServiceInterface


class NominatimGeocodeAdapter(GeocodeServiceInterface):

    """Adapter que consome a API Nominatim do OpenStreetMap para geocodificação"""

    __BASE_URL = "https://nominatim.openstreetmap.org/search"
    __USER_AGENT = "LostFinder/1.0"

    def get_coordinates(self, street: str, neighborhood: str, cep: str) -> dict | None:

        """Obtém as coordenadas geográficas a partir de dados de endereço via API Nominatim

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
            Dicionário com 'latitude' e 'longitude', ou None se não encontrado

        """

        query = f"{street}, {neighborhood}, {cep}"

        params = {
            "q": query,
            "format": "json",
            "limit": 1,
        }

        headers = {
            "User-Agent": self.__USER_AGENT,
        }

        try:

            response = requests.get(
                self.__BASE_URL,
                params=params,
                headers=headers,
                timeout=10,
            )

            response.raise_for_status()

            results = response.json()

            if not results:

                return None

            return {
                "latitude": float(results[0]["lat"]),
                "longitude": float(results[0]["lon"]),
            }

        except (requests.RequestException, KeyError, ValueError, IndexError):

            return None
