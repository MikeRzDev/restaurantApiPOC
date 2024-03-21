from models.RestaurantsModel import RestaurantsModel
from schemas.RestaurantsSchema import RestaurantsSchema

class RestaurantsServices():

    def __init__(self, db) -> None:
      self.db = db

    def getRestaurants(self):
      result = self.db.query(RestaurantsModel).all()
      return result

    def getRestaurant(self, id):
      result = self.db.query(RestaurantsModel).filter(RestaurantsModel.id == id).first()
      return result

    def createRestaurants(self, restaurantsSchema: RestaurantsSchema):
      restaurantsModel = RestaurantsModel(**restaurantsSchema.dict())
      self.db.add(restaurantsModel)
      self.db.commit()
      return

    def deleteRestaurants(self, id: int):
      self.db.query(RestaurantsModel).filter(RestaurantsModel.id == id).delete()
      self.db.commit()
      return

    def updateRestaurants(self, id: int, data: RestaurantsSchema):
      restaurants = self.db.query(RestaurantsModel).filter(RestaurantsModel.id == id).first()
      restaurants.name = data.name
