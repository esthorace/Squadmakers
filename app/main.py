from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse

from .routers import chistes, matematicas

app = FastAPI()

app.include_router(chistes.router)
app.include_router(matematicas.router)


@app.get("/yaml")
async def openapi_yaml():
    rutas = [ruta for ruta in app.routes if ruta.path != "/yaml"]
    openapi_schema = get_openapi(
        title="Squadmakers",
        version="0.0.1",
        description="Aplicación reto",
        routes=rutas,
    )
    return JSONResponse(content=openapi_schema)
