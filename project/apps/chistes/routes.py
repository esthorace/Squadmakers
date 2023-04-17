from fastapi import APIRouter, Query

from ...database import engine
from .controllers import (
    actualizar_chiste_handler,
    eliminar_chiste_handler,
    guardar_chiste_handler,
    obtener_chistes_handler,
)
from .models import ChisteActualizar, ChisteCrear

router = APIRouter()

DESCRIPTION = "pokemon: Chuck o Dad"


@router.get("/chistes")
async def obtener_chistes(query: str | None = Query(None, description=DESCRIPTION)) -> dict:
    return await obtener_chistes_handler(query)


@router.post("/chistes", response_model=ChisteCrear)
async def guardar_chiste(query: str | None = Query(None, description=DESCRIPTION)) -> dict:
    return await guardar_chiste_handler(query)


@router.put("/chistes/{chiste_number}", response_model=ChisteActualizar)
async def actualizar_chiste(chiste_number: int, query: str | None = Query(None, description=DESCRIPTION)):
    return await actualizar_chiste_handler(chiste_number, query)


@router.delete("/chistes/{chiste_number}")
async def eliminar_chiste(chiste_number: int):
    return await eliminar_chiste_handler(chiste_number)
