from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.PersonsModel import PersonsModel
from schemas.PersonsSchema import PersonsSchema
from services.PersonsServices import PersonsServices

persons_router = APIRouter()

@persons_router.get('/persons', tags=['Persons'], response_model=List[PersonsSchema], status_code=200)
def getPersons() -> List[PersonsSchema]:

    db = Session()
    result = PersonsServices(db).getPersons()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@persons_router.get('/persons/{id}', tags=['Persons'], response_model=PersonsSchema)
def getPersons(id: int) -> PersonsSchema:

    db = Session()
    result = PersonsServices(db).getPersons()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@persons_router.post('/persons', tags=['Persons'], response_model=dict, status_code=201)
def createPersons(personsSchema: PersonsSchema) -> dict:

    db = Session()
    PersonsServices(db).createPersons(personsSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@persons_router.put('/persons/{id}', tags=['Persons'], response_model=dict, status_code=200)
def updatePersons(id: int, personsSchema: PersonsSchema)-> dict:

    db = Session()
    result = PersonsServices(db).getPersons(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    PersonsServices(db).updatePersons(id, personsSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@persons_router.delete('/persons/{id}', tags=['Persons'], response_model=dict, status_code=200)
def deletePersons(id: int)-> dict:

    db = Session()
    result: PersonsModel = db.query(PersonsModel).filter(PersonsModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    PersonsServices(db).deletePersons(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
