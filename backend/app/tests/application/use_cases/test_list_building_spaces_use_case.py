from backend.app.application.use_cases.list_building_spaces_use_case import ListBuildingSpacesUseCase
from backend.app.application.dtos.list_building_spaces_input_dto import ListBuildingSpacesInputDTO

from backend.app.domain.entities.building import Building
from backend.app.domain.entities.building_space import BuildingSpace
from backend.app.domain.value_objects.localization import Localization


from unittest.mock import Mock


def test_list_building_spaces_success():

    building_space_repo = Mock()
    building_repo = Mock()

    localization = Localization(
        cep="11111111",
        neighborhood="Bairro 1",
        street="Rua 1",
    )

    building = Building(
        id=1,
        name="Prédio 1",
        associated_localization=localization
    )

    building_space_repo.get_building_spaces_by_building_id.return_value = [
        BuildingSpace(
            id=1,
            name="Sala 1",
            associated_building=building,
        ),
        BuildingSpace(
            id=2,
            name="Sala 2",
            associated_building=building,
        ),
        BuildingSpace(
            id=3,
            name="Sala 3",
            associated_building=building,
        )
    ]

    building_repo.get_building_by_id.return_value = building

    use_case = ListBuildingSpacesUseCase(building_space_repo, building_repo)

    input_dto = ListBuildingSpacesInputDTO(1)

    output_dtos = use_case.execute(input_dto)

    assert len(output_dtos) == 3
    assert output_dtos[0].name == "Sala 1"
    assert output_dtos[1].name == "Sala 2"
    assert output_dtos[2].name == "Sala 3"