import pytest
from app import app, User, Dish

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_register(client):
    data = {
        'name': 'John Doe',
        'email': 'johndoe@example.com',
        'password': 'password123',
        'city': 'Mumbai',
        'cart': [],
        'wallet': 0
    }

    response = client.post('/register', json=data)

    assert response.status_code == 200
    assert response.json == {'message': 'User registered successfully'}

    user = User.objects(email='johndoe@example.com').first()
    assert user is not None
    user.delete()

def test_login(client):
    # Prepare test data
    user = User(
        name='John Doe',
        email='johndoe@example.com',
        password='password123',
        city='Mumbai',
        cart=[],
        wallet=0
    )
    user.save()

    data = {
        'email': 'johndoe@example.com',
        'password': 'password123'
    }

    response = client.post('/login', json=data)

    assert response.status_code == 200
    assert 'id' in response.json
    assert 'wallet' in response.json

    user.delete()

def test_update_wallet(client):
    # Prepare test data
    user = User(
        name='John Doe',
        email='johndoe@example.com',
        password='password123',
        city='Mumbai',
        cart=[],
        wallet=0
    )
    user.save()

    data = {
        'amount': 50
    }

    response = client.post('/updatewallet/' + str(user.id), json=data)

    assert response.status_code == 200
    assert 'wallet' in response.json
    assert response.json['wallet'] == 50

    user.delete()

def test_add_dish(client):
    data = {
        'name': 'Pizza',
        'description': 'Delicious pizza',
        'image': 'https://example.com/pizza.jpg',
        'price': 9.99,
        'stocks': 100,
        'quantity': 0,
        'isAvailable': True
    }

    response = client.post('/adddish', json=data)

    assert response.status_code == 200
    assert response.json == {'message': 'Dish added successfully'}

    dish = Dish.objects(name='Pizza').first()
    assert dish is not None
    dish.delete()

def test_get_dishes(client):
    dish1 = Dish(
        name='Pizza',
        description='Delicious pizza',
        image='https://example.com/pizza.jpg',
        price=9.99,
        stocks=100,
        quantity=0,
        isAvailable=True
    )
    dish1.save()

    dish2 = Dish(
        name='Burger',
        description='Tasty burger',
        image='https://example.com/burger.jpg',
        price=5.99,
        stocks=50,
        quantity=0,
        isAvailable=True
    )
    dish2.save()

    response = client.get('/dishes')

    assert response.status_code == 200
    assert len(response.json) == 2

    dish1.delete()
    dish2.delete()

# Add more test cases for other routes

