import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app


def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Application deployed successfully using Docker" in response.data


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.data == b"OK"


def test_not_found():
    client = app.test_client()
    response = client.get("/invalid")
    assert response.status_code == 404	