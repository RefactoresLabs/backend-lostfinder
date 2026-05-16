from unittest.mock import Mock

from backend.app.presentation.schemas.http_request import HttpRequest
from backend.app.presentation.controllers.get_building_coordinates_controller import GetBuildingCoordinatesController


def test_get_building_coordinates_controller_success():

    fake_use_case = Mock()
    fake_use_case.execute.return_value = {
        "building_id": 1,
        "building_name": "Prédio A",
        "latitude": -23.0,
        "longitude": -46.0
    }

    controller = GetBuildingCoordinatesController(fake_use_case)

    request = HttpRequest(params={"building_id": "1"})

    response = controller.handle(request)

    assert response.status_code == 200
    assert response.body["message"] == "Coordenadas obtidas com sucesso!"
    assert response.body["data"]["building_id"] == 1
    assert response.body["data"]["latitude"] == -23.0

def test_get_building_coordinates_controller_missing_param():

    fake_use_case = Mock()

    controller = GetBuildingCoordinatesController(fake_use_case)

    request = HttpRequest(params={})

    response = controller.handle(request)

    assert response.status_code == 400
    assert response.body["message"] == "Parâmetro building_id é obrigatório"

def test_get_building_coordinates_controller_invalid_param():

    fake_use_case = Mock()

    controller = GetBuildingCoordinatesController(fake_use_case)

    request = HttpRequest(params={"building_id": "abc"})

    response = controller.handle(request)

    assert response.status_code == 400
    assert response.body["message"] == "Parâmetro building_id deve ser um número inteiro"

def test_get_building_coordinates_controller_not_found():

    fake_use_case = Mock()
    fake_use_case.execute.side_effect = ValueError("Prédio não encontrado")

    controller = GetBuildingCoordinatesController(fake_use_case)

    request = HttpRequest(params={"building_id": "999"})

    response = controller.handle(request)

    assert response.status_code == 404
    assert response.body["message"] == "Prédio não encontrado"

def test_get_building_coordinates_controller_geocoding_fails():

    fake_use_case = Mock()
    fake_use_case.execute.side_effect = RuntimeError("Falha na API")

    controller = GetBuildingCoordinatesController(fake_use_case)

    request = HttpRequest(params={"building_id": "1"})

    response = controller.handle(request)

    assert response.status_code == 502
    assert response.body["message"] == "Falha na API"
