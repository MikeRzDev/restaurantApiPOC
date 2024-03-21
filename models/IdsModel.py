from config.database import Base
from sqlalchemy import Column, Integer, String, Float

class IdsModel(Base):

    __tablename__ = "ids"

    id = Column(Integer, primary_key = True)

    number = Column(Integer)

    # 2.One to One Bidirectional
    # classDiagram
    # Ids "1..1" -- "1..1" Persons
