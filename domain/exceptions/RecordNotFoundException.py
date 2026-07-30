from domain.exceptions.base import DomainException

class RecordNotFoundException(DomainException):
    def __init__(self, field:str):
        super().__init__(
            message = f"{field} ای یافت نشد",
            status_code= 404,
            errors= [f"هیچ رکوردی در دیتابیس وجود نداشت !"]
        )
