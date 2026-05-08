from backend.app.infrastructure.database.session_manager import SessionManager
from backend.app.infrastructure.database.database_url_builder import DatabaseURLBuilder

from backend.app.presentation.controllers.factories.building_factories import make_list_buildings_controller


from flask import Flask, jsonify
from dotenv import load_dotenv


import os


def create_building_routes(app: Flask) -> None:

    """Cria rotas de prédios na aplicação Flask

    Parameters
    ----------
    app: Flask
        Aplicação Flask

    """

    load_dotenv()

    @app.route("/buildings", methods=["GET"])
    def list_buildings():

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

            list_buildings_controller = make_list_buildings_controller(session.session)
            http_response = list_buildings_controller.handle()

        return jsonify(http_response.body), http_response.status_code