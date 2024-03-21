from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.RestaurantsModel import RestaurantsModel
from schemas.RestaurantsSchema import RestaurantsSchema
from services.RestaurantsServices import RestaurantsServices

restaurants_router = APIRouter()

@restaurants_router.get('/restaurants', tags=['Restaurants'], response_model=List[RestaurantsSchema], status_code=200)
def getRestaurants() -> List[RestaurantsSchema]:

    db = Session()
    result = RestaurantsServices(db).getRestaurants()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@restaurants_router.get('/restaurants/{id}', tags=['Restaurants'], response_model=RestaurantsSchema)
def getRestaurants(id: int) -> RestaurantsSchema:

    db = Session()
    result = RestaurantsServices(db).getRestaurants()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@restaurants_router.post('/restaurants', tags=['Restaurants'], response_model=dict, status_code=201)
def createRestaurants(restaurantsSchema: RestaurantsSchema) -> dict:

    db = Session()
    RestaurantsServices(db).createRestaurants(restaurantsSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@restaurants_router.put('/restaurants/{id}', tags=['Restaurants'], response_model=dict, status_code=200)
def updateRestaurants(id: int, restaurantsSchema: RestaurantsSchema)-> dict:

    db = Session()
    result = RestaurantsServices(db).getRestaurants(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    RestaurantsServices(db).updateRestaurants(id, restaurantsSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@restaurants_router.delete('/restaurants/{id}', tags=['Restaurants'], response_model=dict, status_code=200)
def deleteRestaurants(id: int)-> dict:

    db = Session()
    result: RestaurantsModel = db.query(RestaurantsModel).filter(RestaurantsModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    RestaurantsServices(db).deleteRestaurants(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
