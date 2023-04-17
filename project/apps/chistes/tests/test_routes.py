from fastapi.testclient import TestClient

from project.main import app

from .... import main

client = TestClient(app)


def test_obtener_chistes():
    response = client.get("/chistes")
    assert response.status_code == 200
    data = response.json()
    assert "chiste" in data
    assert "pokemon" in data


def test_guardar_chiste():
    response = client.post("/chistes")
    assert response.status_code == 200
    data = response.json()
    assert "chiste" in data
    assert "pokemon" in data


def test_actualizar_chiste():
    # Crear un chiste en la base de datos para poder actualizarlo
    response = client.post("/chistes")
    assert response.status_code == 200
    data = response.json()
    chiste_number = data["number"]

    # Actualizar el chiste que se acaba de crear
    response = client.put(f"/chistes/{chiste_number}")
    assert response.status_code == 200
    data = response.json()
    assert "chiste" in data
    assert "pokemon" in data


def test_eliminar_chiste():
    response = client.post("/chistes")
    assert response.status_code == 200
    data = response.json()
    chiste_number = data["number"]

    response = client.delete(f"/chistes/{chiste_number}")
    assert response.status_code == 200
    data = response.json()
    assert data["eliminado"] == True
