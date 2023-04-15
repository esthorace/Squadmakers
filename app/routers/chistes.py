import random

from fastapi import APIRouter, HTTPException, Query
from sqlmodel import Session

from ..controllers.API_solicitud import solicitud
from ..database import engine
from ..models.model_chistes import Chiste, ChisteActualizar, ChisteCrear
from .data.data_chistes import URLS_CHISTES

router = APIRouter()


@router.get("/chistes")
async def obtener_chistes(query: str | None = Query(None, description="pokemon: Chuck o Dad")) -> dict:
    """
    Obtiene chistes de servicios API, no de la base de datos.
    Recibe un parámetro, si es 'Chuk' o 'Dad', devuelve un chiste de la url preestablecida,
    si no recibe parámetro, devuelve un chiste al azar entre las urls que disparan 'Chuk' o 'Dad'
    """
    if query is None:
        query = random.choice(tuple(URLS_CHISTES))

    if query not in URLS_CHISTES:
        raise HTTPException(
            status_code=400, detail=f"Parámetros esperados {[x for x in URLS_CHISTES]}, o ninguno'")

    url = URLS_CHISTES[query]["url"]
    headers = URLS_CHISTES[query]["headers"]
    claves = URLS_CHISTES[query]["claves"]
    chiste = solicitud(url=url, headers=headers, claves=claves)
    return {"chiste": chiste, "pokemon": query}


@router.post("/chistes", response_model=ChisteCrear)
async def guardar_chiste(query: str | None = Query(None, description="pokemon: Chuck o Dad")) -> dict:
    """
    Recibe un chiste de los servicios API y lo guarda en la base de datos
    """
    response = await obtener_chistes(query)
    chiste_text = response["chiste"]
    pokemon_text = response["pokemon"]
    nuevo_chiste = Chiste(chiste=chiste_text, pokemon=pokemon_text)

    with Session(engine) as session:
        session.add(nuevo_chiste)
        session.commit()
        session.refresh(nuevo_chiste)
    return {"chiste": chiste_text, "pokemon": pokemon_text, "number": nuevo_chiste.number}


@router.put("/chistes/{chiste_number}", response_model=ChisteActualizar)
async def actualizar_chiste(chiste_number: int, query: str | None = Query(None, description="pokemon: Chuck o Dad")):
    """
    Recibe como parámetro un número entero que es el id de un chiste guardado en la base de datos.
    Si no existe, devuelve un error. Si existe, lo actualiza por uno nuevo.
    """
    with Session(engine) as session:
        chiste = session.get(Chiste, chiste_number)
        if not chiste:
            raise HTTPException(status_code=404, detail="Chiste no encontrado")

        response = await obtener_chistes(query)
        chiste.chiste = response["chiste"]
        chiste.pokemon = response["pokemon"]
        session.add(chiste)
        session.commit()
        session.refresh(chiste)
        return {"chiste": chiste.chiste, "pokemon": chiste.pokemon}


@router.delete("/chistes/{chiste_number}")
async def eliminar_chiste(chiste_number: int):
    """
    Recibe como parámetro un número entero que es el id de un chiste guardado en la base de datos.
    Si no existe, devuelve un error. Si existe, lo elimina.
    """
    with Session(engine) as session:
        chiste = session.get(Chiste, chiste_number)
        if not chiste:
            raise HTTPException(status_code=404, detail="Chiste no encontrado")
        session.delete(chiste)
        session.commit()
        return {"eliminado": True}
