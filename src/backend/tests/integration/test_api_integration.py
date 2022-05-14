from fastapi.testclient import TestClient
from pytest import fixture
from api.main_api import app


@fixture()
def testClient():
    client = TestClient(app)
    return client


def test_integration(testClient: TestClient):
    response = testClient.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the (Python+FastAPI, Docker, CI/CD, Azure: Pipelines, DevOps, Cloud) - Template v0.0.1"}