# Reto Backend FastAP

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

## Instalación y ejecución

```bash
pip install requirements.txt
uvicorn app.main:app --reload
```

## Tests

```bash
pytest -v
```
