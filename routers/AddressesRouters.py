from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.AddressesModel import AddressesModel
from schemas.AddressesSchema import AddressesSchema
from services.AddressesServices import AddressesServices

addresses_router = APIRouter()

@addresses_router.get('/addresses', tags=['Addresses'], response_model=List[AddressesSchema], status_code=200)
def getAddresses() -> List[AddressesSchema]:

    db = Session()
    result = AddressesServices(db).getAddresses()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@addresses_router.get('/addresses/{id}', tags=['Addresses'], response_model=AddressesSchema)
def getAddresses(id: int) -> AddressesSchema:

    db = Session()
    result = AddressesServices(db).getAddresses()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@addresses_router.post('/addresses', tags=['Addresses'], response_model=dict, status_code=201)
def createAddresses(addressesSchema: AddressesSchema) -> dict:

    db = Session()
    AddressesServices(db).createAddresses(addressesSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@addresses_router.put('/addresses/{id}', tags=['Addresses'], response_model=dict, status_code=200)
def updateAddresses(id: int, addressesSchema: AddressesSchema)-> dict:

    db = Session()
    result = AddressesServices(db).getAddresses(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    AddressesServices(db).updateAddresses(id, addressesSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@addresses_router.delete('/addresses/{id}', tags=['Addresses'], response_model=dict, status_code=200)
def deleteAddresses(id: int)-> dict:

    db = Session()
    result: AddressesModel = db.query(AddressesModel).filter(AddressesModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    AddressesServices(db).deleteAddresses(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
