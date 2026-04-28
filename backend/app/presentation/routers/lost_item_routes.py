from flask import request, jsonify, Flask
from dotenv import load_dotenv


import os


from backend.app.presentation.schemas.http_request import HttpRequest
from backend.app.presentation.controllers.factories.lost_item_factories import make_list_lost_item_summarized_controller
from backend.app.presentation.middlewares.jwt_required import jwt_required

from backend.app.infrastructure.database.session_manager import SessionManager
from backend.app.infrastructure.database.database_url_builder import DatabaseURLBuilder

def create_lost_item_routes(app: Flask) -> None:

    load_dotenv()

    @app.route("/lost_items", methods=["GET"])
    @jwt_required
    def list_lost_items_summarized():

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

            list_lost_item_summarized_controller = make_list_lost_item_summarized_controller(
                session_manager.session
            )

            http_response = list_lost_item_summarized_controller.handle(http_request)
        
        return jsonify(http_response.body), http_response.status_code

        