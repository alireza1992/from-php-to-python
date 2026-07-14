class RecordNotFoundException(Exception):
    def __init__(self, message: str="Record/Entity was not found", status_code = 404):
        self.message = message # redundant but convenient still
        self.status_code = status_code
        super().__init__(self.message)
