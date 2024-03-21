from models.TablesModel import TablesModel
from schemas.TablesSchema import TablesSchema

class TablesServices():

    def __init__(self, db) -> None:
      self.db = db

    def getTables(self):
      result = self.db.query(TablesModel).all()
      return result

    def getTable(self, id):
      result = self.db.query(TablesModel).filter(TablesModel.id == id).first()
      return result

    def createTables(self, tablesSchema: TablesSchema):
      tablesModel = TablesModel(**tablesSchema.dict())
      self.db.add(tablesModel)
      self.db.commit()
      return

    def deleteTables(self, id: int):
      self.db.query(TablesModel).filter(TablesModel.id == id).delete()
      self.db.commit()
      return

    def updateTables(self, id: int, data: TablesSchema):
      tables = self.db.query(TablesModel).filter(TablesModel.id == id).first()
      tables.number = data.number
