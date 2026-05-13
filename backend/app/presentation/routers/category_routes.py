from backend.app.infrastructure.database.session_manager import SessionManager
from backend.app.infrastructure.database.database_url_builder import DatabaseURLBuilder

from backend.app.presentation.controllers.factories.category_factories import make_list_categories_controller
from backend.app.presentation.middlewares.jwt_required import jwt_required


from flask import Flask, jsonify
from dotenv import load_dotenv


import os


def create_category_routes(app: Flask) -> None:

    """Registra as rotas de categorias na aplicação Flask

    Parameters
    ----------
    app: Flask
        Aplicação Flask

    """

    load_dotenv()

    @app.route("/categories", methods=["GET"])
    @jwt_required
    def list_categories():

        database_url = DatabaseURLBuilder.build(
            os.environ["SGBD"],
            {
                "DATABASE": os.environ.get("DATABASE"),
                "USERNAME": os.environ.get("USERNAME"),
                "PASSWORD": os.environ.get("PASSWORD"),
                "HOSTNAME": os.environ.get("HOSTNAME"),
                "PORT": os.environ.get("PORT"),
            },
        )

        with SessionManager(database_url) as session:

            list_categories_controller = make_list_categories_controller(session.session)
            http_response = list_categories_controller.handle()

        return jsonify(http_response.body), http_response.status_code