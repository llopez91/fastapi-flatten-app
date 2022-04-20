import pytest
from fastapi.testclient import TestClient
from main import app


@pytest.fixture
def client():
    client = TestClient(app)
    return client


def test_can_only_post(client):
    resp = client.get("/flatten")
    assert resp.status_code == 405


def test_flatten_basic_success(client):
    resp = client.post("/flatten", json={"data": [[1, 2], [3, 4]]})
    assert resp.status_code == 200
    assert resp.json()['results'] == [1, 2, 3, 4]


def test_flatten_depth_success(client):
    resp = client.post("/flatten", json={"data": [1, [2, [3, [4, 5]]]]})
    assert resp.status_code == 200
    assert resp.json()['results'] == [1, 2, 3, 4, 5]


def test_flatten_not_accept_another_request_than_list(client):
    resp = client.post("/flatten", json={"data": "prueba"})
    assert resp.status_code == 422
