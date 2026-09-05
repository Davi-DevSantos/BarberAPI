from src.repositories.Barber_Repo import BarberRepository 
from src.core.ExceptionsError import *

class BarberService:
    def __init__(self, barber_repository: BarberRepository):
        self.barber_repo = barber_repository

    def create_service(self, data: dict):
        services_id = data.get("id")
        check = self.barber_repo.get_user_by_id(services_id)
        if check:
            raise DuplicateScheduleError("horário já ocupado")
        if data == '':
            raise InvalidInputError("Não pode está vazio")
        service = self.barber_repo.save_data_of_services(**data)
        return service

    def get_all_services(self):
        services = self.barber_repo.get_all_services()
        return services

    def get_service_by_id_or_email(self, service_data: dict):
        service_id = service_data.get("id")
        email = service_data.get("email")

        if service_id:
            service = self.barber_repo.get_service_by_id(service_id)
        elif email:
            service = self.barber_repo.get_service_by_email(email)
        else:
            service = None

        return service
