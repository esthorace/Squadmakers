from pathlib import Path

from sqlmodel import SQLModel, create_engine

BASE_DIR = Path(__file__).resolve().parent
sqlite_nombre_archivo = "database/database.db"
ruta_archivo = BASE_DIR / sqlite_nombre_archivo

sqlite_url = f"sqlite:///{ruta_archivo}"
engine = create_engine(sqlite_url)


def crear_base_de_datos():
    SQLModel.metadata.create_all(engine)
