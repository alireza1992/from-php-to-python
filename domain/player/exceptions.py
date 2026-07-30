from domain.exceptions.base import DomainException

FIELD_NAMES_FA = {
    "email": "ایمیل",
    "phone": "شماره تلفن",
    "username": "نام کاربری",
}

class UniqueConstraintException(DomainException):
    def __init__(self, field:str = 'email'):
        super().__init__(
            message="اطلاعات وارد شده معتبر نمی‌باشد",
            status_code=409,
            errors={field: [f"این {FIELD_NAMES_FA.get(field, field)} قبلا ثبت شده است."]}
        )