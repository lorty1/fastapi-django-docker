from fastapi.testclient import TestClient
from main import app


client = TestClient(app)


def test_read_list_product():
    response = client.get('/api/products/')
    assert response.status_code == 200


def test_create_product_success():
    response = client.post(
        '/api/products/',
        json={"title": "Foo Bar", "is_active": "false"})
    assert response.status_code == 200


def test_create_error_title():
    response = client.post(
        '/api/products/',
        json={"description": "fdfdf", "is_active": "false"}
    )
    assert response.status_code == 400
    assert response.json()['detail'] == "Un titre est requis !"
