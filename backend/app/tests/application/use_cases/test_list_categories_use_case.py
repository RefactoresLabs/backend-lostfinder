from backend.app.application.use_cases.list_categories_use_case import ListCategoriesUseCase

from backend.app.domain.entities.category import Category


from unittest.mock import Mock


def test_list_categories_success():

    repo = Mock()

    repo.get_all_categories.return_value = [
        Category(1, "Material Escolar"),
        Category(2, "Documento")
    ]

    use_case = ListCategoriesUseCase(repo)

    dtos = use_case.execute()

    assert len(dtos) == 2
    assert dtos[0].name == "Material Escolar"
    assert dtos[1].name == "Documento"