from config.database import Base
from sqlalchemy import Column, Integer, String, Float

class TablesModel(Base):

    __tablename__ = "tables"

    id = Column(Integer, primary_key = True)

    number = Column(Integer)

    # 5. Many to One Bidirectional
    # classDiagram
    # Tables "0..*" -- "0..1" Restaurants
