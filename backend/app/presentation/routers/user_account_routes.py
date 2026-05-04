from flask import request, jsonify, Flask
from dotenv import load_dotenv


import os


from backend.app.presentation.schemas.http_request import HttpRequest
from backend.app.presentation.controllers.factories.user_account_factories import make_register_user_account_controller

from backend.app.infrastructure.database.session_manager import SessionManager
from backend.app.infrastructure.database.database_url_builder import DatabaseURLBuilder

def create_user_account_routes(app: Flask) -> None:

    load_dotenv()

    @app.route("/users", methods=["POST"])
    def register_user_account():

        database_url = DatabaseURLBuilder.build(
            os.environ["SGBD"],
            {
                "DATABASE": os.environ["DATABASE"]
            },
        )

        with SessionManager(database_url) as session_manager:

            http_request = HttpRequest(
                body=request.get_json()
            )

            register_user_account_controler = make_register_user_account_controller(
                session_manager.session
            )

            http_response = register_user_account_controler.handle(http_request)
        
        return jsonify(http_response.body), http_response.status_code

        