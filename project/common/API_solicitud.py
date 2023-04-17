import orjson
import requests
from fastapi import HTTPException


def obtener_json_por_clave(respuesta_dict: dict, claves: list[str]) -> dict:
    for clave in claves:
        if isinstance(respuesta_dict, dict) and clave in respuesta_dict:
            respuesta_dict = respuesta_dict[clave]
    return respuesta_dict


def solicitud(url: str,
              headers: dict,
              params: dict | None = None,
              metodo: str = "GET",
              claves: list[str] | None = None
              ) -> dict | None:
    try:
        if metodo == "GET":
            response = requests.get(url, headers=headers, params=params)
        elif metodo == "POST":
            response = requests.get(url, headers=headers, params=params)
        else:
            raise ValueError(f"Método HTTP no válido: {metodo}")
    except requests.RequestException as exc:
        raise HTTPException(
            status_code=400, detail=f"Problemas en cargar datos de la API: {exc}")
    else:
        try:
            json_dict: dict = orjson.loads(response.text)
        except ValueError:
            raise HTTPException(
                status_code=400, detail="La respuesta no es un JSON válido")
        else:
            if claves:
                json_solicitado = obtener_json_por_clave(json_dict, claves)
                return json_solicitado
            return json_dict
