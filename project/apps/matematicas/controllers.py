import math


async def minimo_multiplo_comun_handler(numbers):
    """
    Recibe una lista de números enteros y devuelve su mínimo común múltiplo.
    """
    mcm = numbers[0]
    for n in numbers[1:]:
        mcm = mcm * n // math.gcd(mcm, n)
    return {"mínimo común múltiplo": mcm}


async def incrementar_numero_handler(number):
    """
    Recibe un número entero y devuelve ese número + 1.
    """
    return {"resultado": number + 1}
