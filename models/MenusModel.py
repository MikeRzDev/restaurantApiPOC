from config.database import Base
from sqlalchemy import Column, Integer, String, Float

class MenusModel(Base):

    __tablename__ = "menus"

    id = Column(Integer, primary_key = True)

    name = Column(String)
