import pytest
from fastapi.testclient import TestClient
from app.main import app


class TestPetStore:

    def test_0(self):
        assert True

    def test_get_by_id(self):

        expected_response = {
            "id": 3,
            "category": {"id": 2, "name": "Cats"},
            "name": "tag3",
            "photoUrls": ["url1", "url2"],
            "tags": [{"id": 1, "name": "tag3"}, {"id": 2, "name": "tag4"}],
            "status": "pending",
        }

        client = TestClient(app)

        response = client.get("/pet_store/3")
        assert response.status_code == 200
        assert response.json() == expected_response
