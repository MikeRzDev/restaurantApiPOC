from config.database import Base
from sqlalchemy import Column, Integer, String, Float

class ReservationsModel(Base):

    __tablename__ = "reservations"

    id = Column(Integer, primary_key = True)

    number = Column(Integer)

    # 3.Many to One Unidirectional
    # classDiagram
    # Reservations "0..*" --> "0..1" Tables
