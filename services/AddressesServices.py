from models.AddressesModel import AddressesModel
from schemas.AddressesSchema import AddressesSchema

class AddressesServices():

    def __init__(self, db) -> None:
      self.db = db

    def getAddresses(self):
      result = self.db.query(AddressesModel).all()
      return result

    def getAddresse(self, id):
      result = self.db.query(AddressesModel).filter(AddressesModel.id == id).first()
      return result

    def createAddresses(self, addressesSchema: AddressesSchema):
      addressesModel = AddressesModel(**addressesSchema.dict())
      self.db.add(addressesModel)
      self.db.commit()
      return

    def deleteAddresses(self, id: int):
      self.db.query(AddressesModel).filter(AddressesModel.id == id).delete()
      self.db.commit()
      return

    def updateAddresses(self, id: int, data: AddressesSchema):
      addresses = self.db.query(AddressesModel).filter(AddressesModel.id == id).first()
      addresses.address = data.address
