import json
import pytest

from app import app


@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_get_weather_existing_city(client):
    response = client.get('/weather/San Francisco')
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data == {'temperature': 14, 'weather': 'Cloudy'}


def test_get_weather_nonexistent_city(client):
    response = client.get('/weather/Nonexistent City')
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 404
    assert data == {'error': 'City not found'}


def test_add_weather(client):
    data = {
        'city': 'London',
        'temperature': 18,
        'weather': 'Rainy'
    }
    response = client.post('/weather', json=data)
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data == {'message': 'Weather added successfully'}


def test_update_weather(client):
    data = {
        'temperature': 25,
        'weather': 'Sunny'
    }
    response = client.put('/weather/Los Angeles', json=data)
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data == {'message': 'Weather updated successfully'}


def test_delete_weather(client):
    response = client.delete('/weather/Seattle')
    data = json.loads(response.get_data(as_text=True))
    assert response.status_code == 200
    assert data == {'message': 'Weather deleted successfully'}