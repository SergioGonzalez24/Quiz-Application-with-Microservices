from app import app
import pytest

def test_flask_app():
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200

