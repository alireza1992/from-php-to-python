class ApiCallTimeoutException(Exception):
    def __init__(self,message:str = "Api call was timed out, please try again later."):
        self.message = message
        super().__init__(self.message)