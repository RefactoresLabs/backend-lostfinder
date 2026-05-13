from flask import Flask
from flask_cors import CORS

from backend.app.presentation.routers.user_account_routes import create_user_account_routes
from backend.app.presentation.routers.login_routes import create_login_routes
from backend.app.presentation.routers.lost_item_routes import create_lost_item_routes
from backend.app.presentation.routers.found_item_routes import create_found_item_routes
from backend.app.presentation.routers.category_routes import create_category_routes
from backend.app.presentation.routers.building_routes import create_building_routes
from backend.app.presentation.routers.building_space_routes import create_building_space_routes
from backend.app.presentation.routers.upload_routes import create_upload_routes

def create_app() -> Flask:

    """Cria a interface da aplicação entre o cliente e servidor, com as respectivas rotas

    Returns
    -------
    Flask
        Objeto que atua como interface entre o cliente e servidor

    """

    app = Flask(__name__)
    CORS(app)

    create_user_account_routes(app) # Rotas das contas de usuários
    create_login_routes(app)         # Rotas de autenticação
    create_lost_item_routes(app)     # Rotas de itens perdidos
    create_found_item_routes(app)    # Rotas de itens encontrados
    create_upload_routes(app)  # Rotas de upload de arquivos
    create_category_routes(app) # Rotas de categorias
    create_building_routes(app) # Rotas de prédios
    create_building_space_routes(app) # Rotas de espaços de prédio
    
    return app
