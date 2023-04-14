import random

from fastapi import APIRouter, HTTPException, Query

from ..controllers.API_solicitud import solicitud
from ..data.data_chistes import URLS_CHISTES

router = APIRouter()


@router.get("/chistes")
async def get_chiste(query: str | None = Query(None, description="pokemon: Chuck o Dad")) -> dict:
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
