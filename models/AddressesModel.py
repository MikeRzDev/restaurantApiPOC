from config.database import Base
from sqlalchemy import Column, Integer, String, Float

class AddressesModel(Base):

    __tablename__ = "addresses"

    id = Column(Integer, primary_key = True)

    address = Column(String)
