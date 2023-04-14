import random

import httpx
from fastapi import APIRouter, HTTPException

router = APIRouter()

chistes_tipo = {
    "Chuck": {
        "url": "https://api.chucknorris.io/jokes/random",
        "headers": {},
        "clave": "value"
    },
    "Dad": {
        "url": "https://icanhazdadjoke.com/",
        "headers":  {"Accept": "application/json"},
        "clave": "joke"
    }
}


def solicitud(url, headers, clave):
    try:
        response = httpx.get(url, headers=headers)
    except httpx.RequestError:
        raise HTTPException(
            status_code=400, detail="Problemas en cargar datos de la API")
    else:
        resultado_dict: dict = response.json()
        chiste = resultado_dict.get(clave)
        return chiste


@router.get("/chistes")
async def get_chiste(param: str | None = None):
    if param:
        if param in chistes_tipo:
            url, headers, clave = chistes_tipo[param].values()
            chiste = solicitud(url, headers, clave)
        else:
            raise HTTPException(
                status_code=400, detail=f"Parámetros esperados {[x for x in chistes_tipo]}, o ninguno'")
    else:
        azar = random.choice(tuple(chistes_tipo))
        url, headers, clave = chistes_tipo[azar].values()
        chiste = solicitud(url, headers, clave)
    return {"chiste": chiste}
