from backend.app.application.use_cases.list_buildings_use_case import ListBuildingsUseCase

from backend.app.domain.entities.building import Building
from backend.app.domain.value_objects.localization import Localization


from unittest.mock import Mock


def test_list_buildings_success():

    repo = Mock()

    repo.get_all_buildings.return_value = [
        Building(
            id=1,
            name="Prédio 1",
            associated_localization=Localization(
                cep="111111",
                neighborhood="Bairro 1",
                street="Rua 1"
            )
        ),
        Building(
            id=2,
            name="Prédio 2",
            associated_localization=Localization(
                cep="222222",
                neighborhood="Bairro 2",
                street="Rua 2"
            )
        ),
    ]

    use_case = ListBuildingsUseCase(repo)

    dtos = use_case.execute()

    assert len(dtos) == 2
    assert dtos[0].name == "Prédio 1"
    assert dtos[1].name == "Prédio 2"