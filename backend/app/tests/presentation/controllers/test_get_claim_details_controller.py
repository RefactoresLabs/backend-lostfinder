from backend.app.presentation.controllers.get_claim_details_controller import GetClaimDetailsController
from backend.app.presentation.schemas.http_request import HttpRequest
from backend.app.application.dtos.get_claim_details_output_dto import GetClaimDetailsOutputDTO
from backend.app.domain.exceptions.claim_doesnt_exist_error import ClaimDoesntExistError

from unittest.mock import Mock


def test_get_claim_details_controller_success():

    use_case = Mock()

    use_case.execute.return_value = GetClaimDetailsOutputDTO(
        claim_id=1,
        status_name="Pendente",
        claimant_user_name="Link",
        claimant_user_phone="12345678",
        associated_found_item_id=10,
        associated_found_item_name="Master Sword",
        associated_found_item_user_name="Mario",
        associated_found_item_user_phone="87654321",
        created_at="2026-05-16T12:00:00Z",
        retrieval_code=""
    )

    controller = GetClaimDetailsController(use_case)

    http_response = controller.handle(
        HttpRequest(params={"claim_id": 1})
    )

    assert http_response.status_code == 200
    assert http_response.body["id"] == 1
    assert http_response.body["status"]["name"] == "Pendente"
    assert http_response.body["associated_found_item"]["name"] == "Master Sword"
    assert http_response.body["associated_found_item"]["user"]["name"] == "Mario"
    assert http_response.body["retrieval_code"] == ""


def test_get_claim_details_controller_when_id_not_exists():

    use_case = Mock()
    use_case.execute.side_effect = ClaimDoesntExistError

    controller = GetClaimDetailsController(use_case)

    http_response = controller.handle(
        HttpRequest(params={"claim_id": 1})
    )

    assert http_response.status_code == 404
    assert http_response.body["code"] == "CLAIM_DOESNT_EXIST_ERROR"
