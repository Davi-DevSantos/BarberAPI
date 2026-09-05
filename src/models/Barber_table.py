from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, String, ForeignKey
from src.database.Base import Base

class BarberTable(Base):
    __tablename__ = "barber_table"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)
    telephone: Mapped[str] = mapped_column(String(20), nullable=False)
    optional_email: Mapped[str] = mapped_column(String(50), nullable=True)
    services: Mapped[str] = mapped_column(String(255), nullable=False)
    price: Mapped[int] = mapped_column(Integer, nullable=False)
    date: Mapped[str] = mapped_column(String(255), nullable=False)
    hour: Mapped[str] = mapped_column(String(255), nullable=False)
    