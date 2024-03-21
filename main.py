from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler

from routers.PersonsRouters import persons_router
from routers.IdsRouters import ids_router
from routers.AddressesRouters import addresses_router
from routers.TablesRouters import tables_router
from routers.ReservationsRouters import reservations_router
from routers.RestaurantsRouters import restaurants_router
from routers.MenusRouters import menus_router

app = FastAPI()
app.title = "ejb. LesXon Engine"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)

app.include_router(persons_router)
app.include_router(ids_router)
app.include_router(addresses_router)
app.include_router(tables_router)
app.include_router(reservations_router)
app.include_router(restaurants_router)
app.include_router(menus_router)

Base.metadata.create_all(bind=engine)

@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>ejb. LesXon Engine</h1>')

