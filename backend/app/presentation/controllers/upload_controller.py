# backend/app/presentation/controllers/upload_controller.py

from backend.app.application.use_cases.upload_file_use_case import UploadFileUseCase
from backend.app.infrastructure.storage.local_storage import LocalStorage

class UploadController:
    def __init__(self):
        self.use_case = UploadFileUseCase(LocalStorage())

    def upload(self, file):
        return self.use_case.execute(file)