from flask import request, jsonify
from backend.app.infrastructure.storage.local_storage import LocalStorage

def create_upload_routes(app):

    storage = LocalStorage()

    @app.route("/upload", methods=["POST"])
    def upload():
        file = request.files.get("file")

        if not file:
            return jsonify({"error": "Arquivo não enviado"}), 400

        if not file.content_type.startswith("image/"):
            return jsonify({"error": "Arquivo inválido"}), 400

        path = storage.save(file)

        return jsonify({
            "url": path
        })