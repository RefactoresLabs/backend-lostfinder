import os
from uuid import uuid4

UPLOAD_DIR = "uploads/"

class LocalStorage:
    def save(self, file):
        os.makedirs(UPLOAD_DIR, exist_ok=True)

        filename = f"{uuid4()}_{file.filename}"
        path = os.path.join(UPLOAD_DIR, filename)

        with open(path, "wb") as buffer:
            buffer.write(file.read()) 

        return path