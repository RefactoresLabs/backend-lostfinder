from backend.app.infrastructure.database.session_manager import SessionManager
from backend.app.infrastructure.database.database_url_builder import DatabaseURLBuilder

from backend.app.presentation.controllers.factories.building_space_factories import make_list_building_spaces_controller
from backend.app.presentation.schemas.http_request import HttpRequest


from flask import Flask, jsonify
from dotenv import load_dotenv


import os


def create_building_space_routes(app: Flask) -> None:

    """Cria rotas de espaços de prédio na aplicação Flask

    Parameters
    ----------
    app: Flask
        Aplicação Flask

    """

    load_dotenv()

    @app.route("/buildings/<building_id>/building-spaces", methods=["GET"])
    def list_building_spaces(building_id: int):

        database_url = DatabaseURLBuilder.build(
            os.environ["SGBD"],
            {
                "DATABASE": os.environ.get("DATABASE"),
                "USERNAME": os.environ.get("USERNAME"),
                "PASSWORD": os.environ.get("PASSWORD"),
                "HOSTNAME": os.environ.get("HOSTNAME"),
                "PORT": os.environ.get("PORT"), 
            }
        )

        with SessionManager(database_url) as session:

            http_request = HttpRequest(
                params={
                    "building_id": building_id
                }
            )

            list_buildings_spaces_controller = make_list_building_spaces_controller(session.session)
            http_response = list_buildings_spaces_controller.handle(http_request)

        return jsonify(http_response.body), http_response.status_code