from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from src.core.ExceptionsError import *
from src.database.connection import get_db
from src.repositories.Barber_Repo import BarberRepository
from src.schemas.customer_valid import CustomerValid
from src.services.services_barber import BarberService

router = APIRouter(prefix="/schedule", tags=["agendar", ["schedule"]])

def get_barber_services(db: Session = Depends(get_db)):
    return BarberService(BarberRepository(db))

@router.post("/registrar", response_model=CustomerValid, status_code=status.HTTP_201_CREATED)
def create_schedule(
    body: CustomerValid, service: BarberService = Depends(get_barber_services)
) -> dict:
    try:
        return service.create_service(body)
    except DuplicateScheduleError as e:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(e) ) from e







