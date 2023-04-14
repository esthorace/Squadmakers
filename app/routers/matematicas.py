import math

from fastapi import APIRouter, Query

router = APIRouter()


@router.get("/matematica")
async def mínimo_múltiplo_común(numbers: list[int] = Query(..., description="Lista de números enteros")):
    """
    Recibe una lista de números enteros y devuelve su mínimo común múltiplo.
    """
    mcm = numbers[0]
    for n in numbers[1:]:
        mcm = mcm * n // math.gcd(mcm, n)
    return {"mínimo común múltiplo": mcm}


@router.get("/matematica/sumar_uno")
async def incrementar_número(number: int = Query(..., description="Número entero a incrementar +1")):
    """
    Recibe un número entero y devuelve ese número + 1.
    """
    return {"resultado": number + 1}
