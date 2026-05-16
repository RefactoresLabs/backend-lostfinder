from flask import request, jsonify, Flask
from dotenv import load_dotenv
import os

from backend.app.infrastructure.database.database_url_builder import DatabaseURLBuilder
from backend.app.infrastructure.database.session_manager import SessionManager
from backend.app.presentation.schemas.http_request import HttpRequest
from backend.app.presentation.controllers.factories.claim_factories import (
    make_create_claim_controller,
    make_get_claim_details_controller,
    make_delete_claim_controller,
)
from backend.app.presentation.middlewares.jwt_required import jwt_required


def create_claim_routes(app: Flask) -> None:

    """Registra as rotas de negociação de recuperação de item na aplicação Flask

    Parameters
    ----------
    app: Flask
        Aplicação Flask

    """

    load_dotenv()

    @app.route("/claims", methods=["POST"])
    @jwt_required
    def create_claim():

        database_url = DatabaseURLBuilder.build(
            os.environ["SGBD"],
            {
                "DATABASE": os.environ.get("DATABASE"),
                "USERNAME": os.environ.get("USERNAME"),
                "PASSWORD": os.environ.get("PASSWORD"),
                "HOSTNAME": os.environ.get("HOSTNAME"),
                "DATABASE_PORT": os.environ.get("DATABASE_PORT"),
            },
        )

        with SessionManager(database_url) as session_manager:

            http_request = HttpRequest(
                params={
                    "user_id": request.user_payload["user_id"]
                },
                body=request.get_json(),
            )

            create_claim_controller = make_create_claim_controller(session_manager.session)
            http_response = create_claim_controller.handle(http_request)

        return jsonify(http_response.body), http_response.status_code

    @app.route("/claim/<int:claim_id>", methods=["GET"])
    @jwt_required
    def get_claim_details(claim_id):

        database_url = DatabaseURLBuilder.build(
            os.environ["SGBD"],
            {
                "DATABASE": os.environ.get("DATABASE"),
                "USERNAME": os.environ.get("USERNAME"),
                "PASSWORD": os.environ.get("PASSWORD"),
                "HOSTNAME": os.environ.get("HOSTNAME"),
                "DATABASE_PORT": os.environ.get("DATABASE_PORT"),
            },
        )

        with SessionManager(database_url) as session_manager:

            http_request = HttpRequest(
                params={"claim_id": claim_id},
            )

            get_claim_details_controller = make_get_claim_details_controller(
                session_manager.session,
            )

            http_response = get_claim_details_controller.handle(http_request)

        return jsonify(http_response.body), http_response.status_code

    @app.route("/claim/<int:claim_id>", methods=["DELETE"])
    @jwt_required
    def delete_claim(claim_id):

        database_url = DatabaseURLBuilder.build(
            os.environ["SGBD"],
            {
                "DATABASE": os.environ.get("DATABASE"),
                "USERNAME": os.environ.get("USERNAME"),
                "PASSWORD": os.environ.get("PASSWORD"),
                "HOSTNAME": os.environ.get("HOSTNAME"),
                "DATABASE_PORT": os.environ.get("DATABASE_PORT"),
            },
        )

        with SessionManager(database_url) as session_manager:

            http_request = HttpRequest(
                params={"claim_id": claim_id},
            )

            delete_claim_controller = make_delete_claim_controller(
                session_manager.session,
            )

            http_response = delete_claim_controller.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
