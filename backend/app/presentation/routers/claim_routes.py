from flask import request, jsonify, Flask
from dotenv import load_dotenv
import os

from backend.app.presentation.schemas.http_request import HttpRequest
from backend.app.presentation.controllers.factories.claim_factories import (
    make_get_claim_details_controller,
    make_delete_claim_controller,
)
from backend.app.presentation.middlewares.jwt_required import jwt_required
from backend.app.infrastructure.database.session_manager import SessionManager
from backend.app.infrastructure.database.database_url_builder import DatabaseURLBuilder


def create_claim_routes(app: Flask) -> None:

    """Registra rotas de claim na aplicação Flask"""

    load_dotenv()

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
                "PORT": os.environ.get("DATABASE_PORT"),
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
                "PORT": os.environ.get("DATABASE_PORT"),
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
