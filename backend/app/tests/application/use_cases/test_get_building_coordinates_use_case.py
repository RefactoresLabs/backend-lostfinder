from unittest.mock import Mock
import pytest

from backend.app.application.use_cases.get_building_coordinates_use_case import GetBuildingCoordinatesUseCase
from backend.app.domain.entities.building import Building
from backend.app.domain.value_objects.localization import Localization


def test_get_building_coordinates_success():

    fake_building_repo = Mock()
    fake_geocode_service = Mock()

    localization = Localization(cep="12345-678", neighborhood="Centro", street="Rua Principal")
    building = Building(id=1, name="Prédio A", associated_localization=localization)

    fake_building_repo.get_building_by_id.return_value = building
    fake_geocode_service.get_coordinates.return_value = {"latitude": -23.5505, "longitude": -46.6333}

    use_case = GetBuildingCoordinatesUseCase(
        building_repository=fake_building_repo,
        geocode_service=fake_geocode_service,
    )

    result = use_case.execute(1)

    assert result["building_id"] == 1
    assert result["building_name"] == "Prédio A"
    assert result["latitude"] == -23.5505
    assert result["longitude"] == -46.6333

    fake_building_repo.get_building_by_id.assert_called_once_with(1)
    fake_geocode_service.get_coordinates.assert_called_once_with(
        street="Rua Principal",
        neighborhood="Centro",
        cep="12345-678"
    )

def test_get_building_coordinates_building_not_found():

    fake_building_repo = Mock()
    fake_geocode_service = Mock()

    fake_building_repo.get_building_by_id.return_value = None

    use_case = GetBuildingCoordinatesUseCase(
        building_repository=fake_building_repo,
        geocode_service=fake_geocode_service,
    )

    with pytest.raises(ValueError) as exc:
        use_case.execute(999)

    assert str(exc.value) == "Prédio não encontrado"
    fake_geocode_service.get_coordinates.assert_not_called()

def test_get_building_coordinates_geocoding_fails():

    fake_building_repo = Mock()
    fake_geocode_service = Mock()

    localization = Localization(cep="123", neighborhood="Bairro", street="Rua")
    building = Building(id=1, name="Prédio Oculto", associated_localization=localization)

    fake_building_repo.get_building_by_id.return_value = building
    fake_geocode_service.get_coordinates.return_value = None

    use_case = GetBuildingCoordinatesUseCase(
        building_repository=fake_building_repo,
        geocode_service=fake_geocode_service,
    )

    with pytest.raises(RuntimeError) as exc:
        use_case.execute(1)

    assert str(exc.value) == "Não foi possível obter as coordenadas do prédio"
