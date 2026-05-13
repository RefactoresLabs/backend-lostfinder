from flask import request, jsonify, Flask
from dotenv import load_dotenv


import os
import re


from backend.app.presentation.schemas.http_request import HttpRequest
from backend.app.presentation.controllers.factories.lost_item_factories import (
        make_list_lost_item_summarized_controller,
        make_create_lost_item_controller,
        make_get_lost_item_details_controller,
        make_list_user_account_lost_item_summarized_controller
)
from backend.app.presentation.middlewares.jwt_required import jwt_required

from backend.app.infrastructure.database.session_manager import SessionManager
from backend.app.infrastructure.database.database_url_builder import DatabaseURLBuilder


def create_lost_item_routes(app: Flask) -> None:

    """Registra as rotas de itens perdidos na aplicação Flask

    Parameters
    ----------
    app: Flask
        Objeto que atua como interface entre o cliente e servidor

    """

    load_dotenv()

    @app.route("/lost-items", methods=["POST"])
    @jwt_required
    def create_lost_item():

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

        with SessionManager(database_url) as session_manager:

            http_request = HttpRequest(        
                body=request.get_json(),
                params={"user_id": request.user_payload["user_id"]},
            )

            create_lost_item_controller = make_create_lost_item_controller(
                session_manager.session
            )

            http_response = create_lost_item_controller.handle(http_request)

        return jsonify(http_response.body), http_response.status_code


    @app.route("/lost-items", methods=["GET"])
    @jwt_required
    def list_lost_items_summarized():

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

        with SessionManager(database_url) as session_manager:

            limit = int(request.args.get("limit", 0))
            body = request.get_json() if request.data else {}

            http_request = HttpRequest(
                params={"limit": limit},
                body=body
            )

            list_lost_item_summarized_controller = make_list_lost_item_summarized_controller(
                session_manager.session
            )

            http_response = list_lost_item_summarized_controller.handle(http_request)
        
        return jsonify(http_response.body), http_response.status_code
    
    @app.route("/lost-items/<item_id>", methods=["GET"])
    @jwt_required
    def get_lost_item_details(item_id: int):

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

        with SessionManager(database_url) as session_manager:

            http_request = HttpRequest(
                params={
                    "item_id": item_id,
                },
            )

            get_lost_item_details_controller = make_get_lost_item_details_controller(
                session_manager.session,
            )

            http_response = get_lost_item_details_controller.handle(http_request)

            return jsonify(http_response.body), http_response.status_code
    
    @app.route("/my-lost-items", methods=["GET"])
    @jwt_required
    def list_user_account_lost_items_summarized():

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

        with SessionManager(database_url) as session_manager:

            http_request = HttpRequest(
                params={
                    "user_id": request.user_payload["user_id"],
                },
            )

            list_user_account_lost_item_summarized_controller = make_list_user_account_lost_item_summarized_controller(
                session_manager.session,
            )

            http_response = list_user_account_lost_item_summarized_controller.handle(http_request)

            return jsonify(http_response.body), http_response.status_code


