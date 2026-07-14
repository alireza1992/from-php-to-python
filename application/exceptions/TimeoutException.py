class TimeoutException(Exception):
    def __init__(self,message:str ="Operation timed out", status_code:int=408):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)