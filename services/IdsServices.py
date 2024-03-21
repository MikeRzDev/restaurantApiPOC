from models.IdsModel import IdsModel
from schemas.IdsSchema import IdsSchema

class IdsServices():

    def __init__(self, db) -> None:
      self.db = db

    def getIds(self):
      result = self.db.query(IdsModel).all()
      return result

    def getId(self, id):
      result = self.db.query(IdsModel).filter(IdsModel.id == id).first()
      return result

    def createIds(self, idsSchema: IdsSchema):
      idsModel = IdsModel(**idsSchema.dict())
      self.db.add(idsModel)
      self.db.commit()
      return

    def deleteIds(self, id: int):
      self.db.query(IdsModel).filter(IdsModel.id == id).delete()
      self.db.commit()
      return

    def updateIds(self, id: int, data: IdsSchema):
      ids = self.db.query(IdsModel).filter(IdsModel.id == id).first()
      ids.number = data.number
