from flask import jsonify, Flask
from dotenv import load_dotenv

import os

from backend.app.presentation.schemas.http_request import HttpRequest
from backend.app.presentation.controllers.factories.building_factories import make_get_building_coordinates_controller

from backend.app.infrastructure.database.session_manager import SessionManager
from backend.app.infrastructure.database.database_url_builder import DatabaseURLBuilder


def create_building_routes(app: Flask) -> None:

    """Registra as rotas de prédios na aplicação Flask

    Parameters
    ----------
    app: Flask
        Objeto que atua como interface entre o cliente e servidor

    """

    load_dotenv()

    @app.route("/buildings/<int:building_id>/coordinates", methods=["GET"])
    def get_building_coordinates(building_id):

        database_url = DatabaseURLBuilder.build(
            os.environ["SGBD"],
            {
                "DATABASE": os.environ["DATABASE"],
            },
        )

        with SessionManager(database_url) as session_manager:

            http_request = HttpRequest(
                params={"building_id": building_id},
            )

            get_building_coordinates_controller = make_get_building_coordinates_controller(
                session_manager.session
            )

            http_response = get_building_coordinates_controller.handle(http_request)

        return jsonify(http_response.body), http_response.status_code
