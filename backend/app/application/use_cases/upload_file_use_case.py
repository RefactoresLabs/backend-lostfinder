

class UploadFileUseCase:
    def __init__(self, storage):
        self.storage = storage

    def execute(self, file):
        # validação básica
        if not file.content_type.startswith("image/"):
            raise Exception("Arquivo não é uma imagem")

        path = self.storage.save(file)

        return {
            "url": path
        }