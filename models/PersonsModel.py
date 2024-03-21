from config.database import Base
from sqlalchemy import Column, Integer, String, Float

class PersonsModel(Base):

    __tablename__ = "persons"

    id = Column(Integer, primary_key = True)

    name1 = Column(String)
    name2 = Column(String)
    lastName1 = Column(String)
    lastName2 = Column(String)

    # 1.One to One Unidirectional
    # classDiagram
    # Persons "0..1" --> "1..1" Addresses

    # 2.One to One Bidirectional
    # classDiagram
    # Persons "1..1" -- "1..1" Ids

    # 7. Many to Many Bidirectional
    # classDiagram
    # Persons "0..*" -- "0..*" Persons

    # 6. Many to Many Unidirectional
    # classDiagram
    # Persons "0..*" --> "0..*" Reservations
