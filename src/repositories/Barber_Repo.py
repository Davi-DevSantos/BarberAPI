from sqlalchemy.orm import Session
from models.Barber_table import BarberTable
    

class BarberRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_user_by_id(self, user_id: int):
        user = self.session.query(BarberTable).filter(BarberTable.id == user_id).first()
        return user

    def get_all_users(self):
        users = self.session.query(BarberTable).all()
        return users

    def get_user_by_email(self, email: str):
        user = self.session.query(BarberTable).filter(BarberTable.email == email).first()
        return user

    def save_data_of_services(self, user_data: dict):
        new_services = BarberTable(**user_data)
        self.session.add(new_services)
        self.session.commit()
        return new_services

    def list_services_by_category(self, services: str):
        services = self.session.query(BarberTable).filter(BarberTable.services == services).all()
        return services
    
    def update_service(self, service_id: int, service_data: dict):
        service = self.session.query(BarberTable).filter(BarberTable.id == service_id).first()
        if service:
            for key, value in service_data.items():
                setattr(service, key, value)
            self.session.commit()
        return service
    
    def delete_service(self, service_id: int):
        service = self.session.query(BarberTable).filter(BarberTable.id == service_id).first()
        if service:
            self.session.delete(service)
            self.session.commit()
        return service