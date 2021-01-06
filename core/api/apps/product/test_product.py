from fastapi.testclient import TestClient
from core.api.main import app
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')
print('mypath',myPath,'-->', sys)

client = TestClient(app)

def test_read_list_product():
    response = client.get('/products/')
    print('products list ? ==>',response.json())
    assert response.status_code == 200

def test_create_product_success():
    response = client.post(
        '/products/',
        json={"title": "Foo Bar", "is_active": "false"})
    print(response.status_code)
    print(response.json())
    assert response.status_code == 200

def test_create_error_title():
    response = client.post(
        '/products/',
        json={"description": "fdfdf","is_active": "false"}
    )
    assert response.status_code == 400
    assert response.json()['detail'] == "Un titre est requis !"