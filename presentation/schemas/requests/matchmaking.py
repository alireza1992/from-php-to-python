from pydantic import BaseModel, field_validator

class MatchmakingValidation(BaseModel):
    xp_level: int

    @field_validator("xp_level")
    @classmethod
    def validate_xp_level(cls, value: int):
        if value not in (10, 11, 12, 13):
            raise ValueError("مقدار وارد شده صحیح نمی‌باشد.")
        return value