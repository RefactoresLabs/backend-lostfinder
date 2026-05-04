import os
from flask import request, jsonify, send_from_directory
from backend.app.infrastructure.storage.local_storage import LocalStorage

UPLOAD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..', 'uploads')

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

    @app.route("/uploads/<path:filename>")
    def serve_upload(filename):
        return send_from_directory(UPLOAD_DIR, filename)