from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.ReservationsModel import ReservationsModel
from schemas.ReservationsSchema import ReservationsSchema
from services.ReservationsServices import ReservationsServices

reservations_router = APIRouter()

@reservations_router.get('/reservations', tags=['Reservations'], response_model=List[ReservationsSchema], status_code=200)
def getReservations() -> List[ReservationsSchema]:

    db = Session()
    result = ReservationsServices(db).getReservations()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@reservations_router.get('/reservations/{id}', tags=['Reservations'], response_model=ReservationsSchema)
def getReservations(id: int) -> ReservationsSchema:

    db = Session()
    result = ReservationsServices(db).getReservations()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@reservations_router.post('/reservations', tags=['Reservations'], response_model=dict, status_code=201)
def createReservations(reservationsSchema: ReservationsSchema) -> dict:

    db = Session()
    ReservationsServices(db).createReservations(reservationsSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@reservations_router.put('/reservations/{id}', tags=['Reservations'], response_model=dict, status_code=200)
def updateReservations(id: int, reservationsSchema: ReservationsSchema)-> dict:

    db = Session()
    result = ReservationsServices(db).getReservations(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    ReservationsServices(db).updateReservations(id, reservationsSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@reservations_router.delete('/reservations/{id}', tags=['Reservations'], response_model=dict, status_code=200)
def deleteReservations(id: int)-> dict:

    db = Session()
    result: ReservationsModel = db.query(ReservationsModel).filter(ReservationsModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    ReservationsServices(db).deleteReservations(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
