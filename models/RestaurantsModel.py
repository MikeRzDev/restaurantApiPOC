from config.database import Base
from sqlalchemy import Column, Integer, String, Float

class RestaurantsModel(Base):

    __tablename__ = "restaurants"

    id = Column(Integer, primary_key = True)

    name = Column(String)

    # 5. One to Many Bidirectional
    # classDiagram
    # Restaurants "0..1" -- "0..*" Tables

    # 4. One to Many Unidirectional
    # classDiagram
    # Restaurants "0..1" --> "0..*" Menus
