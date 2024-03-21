from fastapi import APIRouter
from fastapi import Depends, Path, Query
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, List
from config.database import Session

from models.MenusModel import MenusModel
from schemas.MenusSchema import MenusSchema
from services.MenusServices import MenusServices

menus_router = APIRouter()

@menus_router.get('/menus', tags=['Menus'], response_model=List[MenusSchema], status_code=200)
def getMenus() -> List[MenusSchema]:

    db = Session()
    result = MenusServices(db).getMenus()
    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@menus_router.get('/menus/{id}', tags=['Menus'], response_model=MenusSchema)
def getMenus(id: int) -> MenusSchema:

    db = Session()
    result = MenusServices(db).getMenus()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    return JSONResponse(status_code=200, content=jsonable_encoder(result))

@menus_router.post('/menus', tags=['Menus'], response_model=dict, status_code=201)
def createMenus(menusSchema: MenusSchema) -> dict:

    db = Session()
    MenusServices(db).createMenus(menusSchema)
    return JSONResponse(status_code=201, content={"message": "Se ha registrado"})

@menus_router.put('/menus/{id}', tags=['Menus'], response_model=dict, status_code=200)
def updateMenus(id: int, menusSchema: MenusSchema)-> dict:

    db = Session()
    result = MenusServices(db).getMenus(id)

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    MenusServices(db).updateMenus(id, menusSchema)
    return JSONResponse(status_code=200, content={"message": "Se ha modificado el registro"})

@menus_router.delete('/menus/{id}', tags=['Menus'], response_model=dict, status_code=200)
def deleteMenus(id: int)-> dict:

    db = Session()
    result: MenusModel = db.query(MenusModel).filter(MenusModel.id == id).first()

    if not result:
       return JSONResponse(status_code=404, content={"message": "No encontrado"})

    MenusServices(db).deleteMenus(id)

    return JSONResponse(status_code=200, content={"message": "Se ha eliminado el registro"})
