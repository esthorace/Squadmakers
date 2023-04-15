from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_mínimo_múltiplo_común():
    response = client.get("/matematica", params={"numbers": [4, 6]})
    assert response.status_code == 200
    data = response.json()
    assert "mínimo común múltiplo" in data
    assert data["mínimo común múltiplo"] == 12


def test_incrementar_número():
    response = client.get("/matematica/sumar_uno", params={"number": 3})
    assert response.status_code == 200
    data = response.json()
    assert "resultado" in data
    assert data["resultado"] == 4
