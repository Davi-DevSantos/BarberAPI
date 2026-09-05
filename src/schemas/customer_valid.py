from pydantic import BaseModel, EmailStr, Field, PhoneNumber, field_validator
from typing import Optional, Annotated
import datetime


class CustomerValid(BaseModel):
    name: str = Field(..., min_length=1, max_length=50)
    phone_number: PhoneNumber = None
    email: Optional[EmailStr] = None
    service: str = Field(..., min_length=1, max_length=50)
    data_agendada: Annotated[datetime, Field(..., description="2026-09-06T17:50:00-03:00")]

    @field_validator
    @classmethod
    def validate_datetime(cls, h: datetime) -> datetime:
        if h < datetime.now(h.tzinfo):
            raise ValueError("Horario invalido")
        if not 8 <= h.hour < 19:
            raise ValueError("Barbearia fechada")
        if h.minute not in (0, 30):
            raise ValueError("Só :00 e :30")
        return h

    