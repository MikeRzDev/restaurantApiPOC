from models.ReservationsModel import ReservationsModel
from schemas.ReservationsSchema import ReservationsSchema

class ReservationsServices():

    def __init__(self, db) -> None:
      self.db = db

    def getReservations(self):
      result = self.db.query(ReservationsModel).all()
      return result

    def getReservation(self, id):
      result = self.db.query(ReservationsModel).filter(ReservationsModel.id == id).first()
      return result

    def createReservations(self, reservationsSchema: ReservationsSchema):
      reservationsModel = ReservationsModel(**reservationsSchema.dict())
      self.db.add(reservationsModel)
      self.db.commit()
      return

    def deleteReservations(self, id: int):
      self.db.query(ReservationsModel).filter(ReservationsModel.id == id).delete()
      self.db.commit()
      return

    def updateReservations(self, id: int, data: ReservationsSchema):
      reservations = self.db.query(ReservationsModel).filter(ReservationsModel.id == id).first()
      reservations.number = data.number
