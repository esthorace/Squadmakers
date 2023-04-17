# Reto Backend FastAP

## Instalación y ejecución del proyecto actual

```bash
pip install requirements.txt
uvicorn project.main:app --reload
```

## Tests

```bash
pytest -v
```

## Respuesta a la pregunta

**¿Qué repositorio utilizarías? PostgreSQL, MariaDB, Casandra, MongoDB, ElasticSearch, Oracle, SQL Server**

SQLModel es una biblioteca hecha por el mismo desarrollador de FastAPI para FastAPI. Es una capa de abstracción sobre SQLAlchemy, el cual es compatible con los siguientes motores de bases de datos:

- PostgreSQL
- MySQL
- MariaDB
- SQLite
- Oracle
- Microsoft SQL Server

Si bien hay compatibilidad con ElasticSearch por bibliotecas de terceros, y considerando que los modelos de esta aplicación son simples, y pueden guardarse en una tabla relacional, descartaría el uso de Cassandra y MongoDB para este proyecto puntual.

Con MongoDB, el archivo database.py no sería necesario, ya que no hay una función específica para crear la base de datos porque las bases de datos y las colecciones se crean automáticamente cuando se inserta el primer documento.

```bash
pip install pymongo
```

El archivo models.model_chistes.py quedaría parecido a lo siguiente:

```python
from pymongo import MongoClient

client = MongoClient()
db = client['chistes_db']
chistes_collection = db['chistes']

def crear_chiste(chiste_text: str, pokemon_text: str):
    chiste = {"chiste": chiste_text, "pokemon": pokemon_text}
    chistes_collection.insert_one(chiste)

def obtener_chiste(chiste_id: str):
    return chistes_collection.find_one({"_id": chiste_id})

def actualizar_chiste(chiste_id: str, chiste_text: str, pokemon_text: str):
    chistes_collection.update_one({"_id": chiste_id}, {"$set": {"chiste": chiste_text, "pokemon": pokemon_text}})

def eliminar_chiste(chiste_id: str):
    chistes_collection.delete_one({"_id": chiste_id})
```
