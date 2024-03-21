from models.MenusModel import MenusModel
from schemas.MenusSchema import MenusSchema

class MenusServices():

    def __init__(self, db) -> None:
      self.db = db

    def getMenus(self):
      result = self.db.query(MenusModel).all()
      return result

    def getMenu(self, id):
      result = self.db.query(MenusModel).filter(MenusModel.id == id).first()
      return result

    def createMenus(self, menusSchema: MenusSchema):
      menusModel = MenusModel(**menusSchema.dict())
      self.db.add(menusModel)
      self.db.commit()
      return

    def deleteMenus(self, id: int):
      self.db.query(MenusModel).filter(MenusModel.id == id).delete()
      self.db.commit()
      return

    def updateMenus(self, id: int, data: MenusSchema):
      menus = self.db.query(MenusModel).filter(MenusModel.id == id).first()
      menus.name = data.name
