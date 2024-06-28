import pytest
from fastapi.testclient import TestClient
from src.main import app




class TestEndpoint0:



    
    def test_endpoint_0(self):
        assert True

    def test_read_main(self):

        client = TestClient(app)
                
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"msg": "Hello World"}