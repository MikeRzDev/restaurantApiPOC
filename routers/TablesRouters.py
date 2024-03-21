from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.TablesModel import TablesModel
from schemas.TablesSchema import TablesSchema
from services.TablesServices import TablesServices

tables_router = APIRouter()

@tables_router.get('/tables', tags=['Tables'], response_model=List[TablesSchema], status_code=200)
def getTables() -> List[TablesSchema]:

    db = Session()
    result = TablesServices(db).getTables()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@tables_router.get('/tables/{id}', tags=['Tables'], response_model=TablesSchema)
def getTables(id: int) -> TablesSchema:

    db = Session()
    result = TablesServices(db).getTables()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@tables_router.post('/tables', tags=['Tables'], response_model=dict, status_code=201)
def createTables(tablesSchema: TablesSchema) -> dict:

    db = Session()
    TablesServices(db).createTables(tablesSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@tables_router.put('/tables/{id}', tags=['Tables'], response_model=dict, status_code=200)
def updateTables(id: int, tablesSchema: TablesSchema)-> dict:

    db = Session()
    result = TablesServices(db).getTables(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    TablesServices(db).updateTables(id, tablesSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@tables_router.delete('/tables/{id}', tags=['Tables'], response_model=dict, status_code=200)
def deleteTables(id: int)-> dict:

    db = Session()
    result: TablesModel = db.query(TablesModel).filter(TablesModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    TablesServices(db).deleteTables(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
