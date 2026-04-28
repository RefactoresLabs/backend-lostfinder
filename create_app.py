from flask import Flask

from backend.app.presentation.routers.user_account_routes import create_user_account_routes
from backend.app.presentation.routers.login_routes import create_login_routes
from backend.app.presentation.routers.lost_item_routes import create_lost_item_routes
from backend.app.presentation.routers.found_item_routes import create_found_item_routes

def create_app() -> Flask:

    """Cria a interface da aplicação entre o cliente e servidor, com as respectivas rotas

    Returns
    -------
    Flask
        Objeto que atua como interface entre o cliente e servidor

    """

    app = Flask(__name__)

    create_user_account_routes(app) # Rotas das contas de usuários
    create_login_routes(app)         # Rotas de autenticação
    create_lost_item_routes(app)     # Rotas de itens perdidos
    create_found_item_routes(app)    # Rotas de itens encontrados

    return app
