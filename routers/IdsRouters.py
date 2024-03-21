from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.IdsModel import IdsModel
from schemas.IdsSchema import IdsSchema
from services.IdsServices import IdsServices

ids_router = APIRouter()

@ids_router.get('/ids', tags=['Ids'], response_model=List[IdsSchema], status_code=200)
def getIds() -> List[IdsSchema]:

    db = Session()
    result = IdsServices(db).getIds()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@ids_router.get('/ids/{id}', tags=['Ids'], response_model=IdsSchema)
def getIds(id: int) -> IdsSchema:

    db = Session()
    result = IdsServices(db).getIds()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@ids_router.post('/ids', tags=['Ids'], response_model=dict, status_code=201)
def createIds(idsSchema: IdsSchema) -> dict:

    db = Session()
    IdsServices(db).createIds(idsSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@ids_router.put('/ids/{id}', tags=['Ids'], response_model=dict, status_code=200)
def updateIds(id: int, idsSchema: IdsSchema)-> dict:

    db = Session()
    result = IdsServices(db).getIds(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    IdsServices(db).updateIds(id, idsSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@ids_router.delete('/ids/{id}', tags=['Ids'], response_model=dict, status_code=200)
def deleteIds(id: int)-> dict:

    db = Session()
    result: IdsModel = db.query(IdsModel).filter(IdsModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    IdsServices(db).deleteIds(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
