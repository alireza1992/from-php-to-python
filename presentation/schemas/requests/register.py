from pydantic import BaseModel, EmailStr, field_validator


class RegisterValidation(BaseModel):
    email: EmailStr
    password: str
    referral_code: str | None = None

    @field_validator("password")
    @classmethod
    def validate_password(cls, value:str):
        if len(value) < 6:
            raise ValueError("رمز عبور باید حداقل ۸ کاراکتر باشد.")
        return value
