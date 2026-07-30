class DomainException(Exception):
    def __init__(self, message: str, status_code: int, errors: dict = {}):
        self.message = message
        self.status_code = status_code
        self.errors = errors
        super().__init__(self.message)