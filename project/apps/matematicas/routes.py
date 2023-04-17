from fastapi import APIRouter, Query

from .controllers import incrementar_numero_handler, minimo_multiplo_comun_handler

router = APIRouter()


@router.get("/matematica")
async def minimo_multiplo_comun(numbers: list[int] = Query(..., description="Lista de números enteros")):
    return await minimo_multiplo_comun_handler(numbers)


@router.get("/matematica/sumar_uno")
async def incrementar_numero(number: int = Query(..., description="Número entero a incrementar +1")):
    return await incrementar_numero_handler(number)
