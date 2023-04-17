import random

from fastapi import HTTPException
from sqlmodel import Session

from ...common.API_solicitud import solicitud
from ...database import engine
from .data import URLS_CHISTES
from .models import Chiste


async def obtener_chistes_handler(query: str | None) -> dict:
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


async def guardar_chiste_handler(query: str | None) -> dict:
    """
    Recibe un chiste de los servicios API y lo guarda en la base de datos
    """
    response = await obtener_chistes_handler(query)
    chiste_text = response["chiste"]
    pokemon_text = response["pokemon"]
    nuevo_chiste = Chiste(chiste=chiste_text, pokemon=pokemon_text)

    with Session(engine) as session:
        session.add(nuevo_chiste)
        session.commit()
        session.refresh(nuevo_chiste)
    return {"chiste": chiste_text, "pokemon": pokemon_text, "number": nuevo_chiste.number}


async def actualizar_chiste_handler(chiste_number: int, query: str | None) -> dict:
    """
    Recibe como parámetro un número entero que es el id de un chiste guardado en la base de datos.
    Si no existe, devuelve un error. Si existe, lo actualiza por uno nuevo.
    """
    with Session(engine) as session:
        chiste = session.get(Chiste, chiste_number)
        if not chiste:
            raise HTTPException(status_code=404, detail="Chiste no encontrado")

        response = await obtener_chistes_handler(query)
        chiste.chiste = response["chiste"]
        chiste.pokemon = response["pokemon"]
        session.add(chiste)
        session.commit()
        session.refresh(chiste)
        return {"chiste": chiste.chiste, "pokemon": chiste.pokemon}


async def eliminar_chiste_handler(chiste_number: int) -> dict:
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
