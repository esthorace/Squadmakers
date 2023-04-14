import orjson
import requests
from fastapi import HTTPException


def solicitud(url: str,
              headers: dict,
              params: dict | None = None,
              método: str = "GET",
              claves: list[str] | None = None
              ) -> dict | None:
    try:
        if método == "GET":
            response = requests.get(url, headers=headers, params=params)
        elif método == "POST":
            response = requests.get(url, headers=headers, params=params)
        else:
            raise ValueError(f"Método HTTP no válido: {método}")
    except requests.RequestException as exc:
        raise HTTPException(
            status_code=400, detail="Problemas en cargar datos de la API: {exc}")
    else:
        try:
            respuesta_dict: dict = orjson.loads(response.text)
        except ValueError:
            raise HTTPException(
                status_code=400, detail="La respuesta no es un JSON válido")
        if claves:
            for clave in claves:
                if isinstance(respuesta_dict, dict) and clave in respuesta_dict:
                    respuesta_dict = respuesta_dict[clave]
        return respuesta_dict
