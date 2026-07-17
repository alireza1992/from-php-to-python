class DatabaseConnectionFailedException(Exception):
    def __init__(self, message: str="Database connection failed"):
        self.message = message
        super().__init__(self.message)