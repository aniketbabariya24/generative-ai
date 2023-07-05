from flask import Flask, request, jsonify
from mongoengine import connect, Document, StringField, FloatField, IntField, BooleanField, ReferenceField
from dotenv import load_dotenv
from flask_cors import CORS
import os

load_dotenv()

# Access environment variables
mongoUri = os.getenv('MONGOURI')


app = Flask(__name__)
connect('zomato', host=mongoUri)  # Replace with your MongoDB URI
CORS(app)

# Schema for Users
class User(Document):
    name = StringField(required=True)
    email = StringField(required=True, unique=True)
    password = StringField(required=True)
    city = StringField(required=True)
    wallet = FloatField(default=0)

# Schema for Dishes
class Dish(Document):
    name = StringField(required=True)
    description = StringField(required=True)
    price = FloatField(required=True)
    stocks = IntField(required=True)
    isAvailable = BooleanField(default=True)

# Schema for Orders
class Order(Document):
    dish = ReferenceField(Dish)

# Route for user registration
@app.route('/register', methods=['POST'])
def register():
    name = request.json.get('name')
    email = request.json.get('email')
    password = request.json.get('password')
    city = request.json.get('city')
    wallet = request.json.get('wallet')

    # Create a new user
    user = User(name=name, email=email, password=password, city=city, wallet=wallet)
    user.save()

    return jsonify({'message': 'User registered successfully'})

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    email = request.json.get('email')
    password = request.json.get('password')

    # Check if email and password are provided
    if not email or not password:
        return jsonify({'message': 'Invalid email or password'}), 400

    # Find the user by email
    user = User.objects(email=email).first()
    userId= str(user.id)
    wallet= user.wallet
    response={
        "id":userId,
        "wallet":wallet
    }
    if user and user.password == password:
        return jsonify(response), 200

    # Invalid email or password
    return jsonify({'message': 'Invalid email or password'}), 401


@app.route('/updatewallet/<id>', methods=['POST'])
def update_wallet(id):
    amount = request.json.get('amount')

    # Check if amount is provided
    if not amount:
        return jsonify({'message': 'Invalid amount'}), 400

    # Find the user by id
    user = User.objects(id=id).first()

    # Check if user exists
    if not user:
        return jsonify({'message': 'User not found'}), 404

    
   

    # Update the wallet amount
    user.wallet += amount
    user.save()

    wallet= user.wallet
    response={
        "wallet":wallet
      }

    return jsonify(response), 200


# Route for adding a dish
@app.route('/adddish', methods=['POST'])
def add_dish():
    name = request.json.get('name')
    description = request.json.get('description')
    price = request.json.get('price')
    stocks = request.json.get('stocks')
    is_available = request.json.get('isAvailable', True)

    # Create a new dish
    dish = Dish(name=name,description=description , price=price, stocks=stocks, isAvailable=is_available)
    dish.save()

    return jsonify({'message': 'Dish added successfully'})

# Route for retrieving all dishes
@app.route('/dishes', methods=['GET'])
def get_dishes():
    dishes = Dish.objects()
    dish_list = []

    for dish in dishes:
        dish_data = {
            'name': dish.name,
            'price': dish.price,
            'stocks': dish.stocks,
            'isAvailable': dish.isAvailable
        }
        dish_list.append(dish_data)

    return jsonify(dish_list)

# Route for updating a dish
@app.route('/updatedish/<id>', methods=['PUT'])
def update_dish(id):
    dish = Dish.objects(id=id).first()

    if not dish:
        return jsonify({'message': 'Dish not found'})

    name = request.json.get('name')
    price = request.json.get('price')
    stocks = request.json.get('stocks')
    is_available = request.json.get('isAvailable')

    dish.name = name if name else dish.name
    dish.price = price if price else dish.price
    dish.stocks = stocks if stocks else dish.stocks
    dish.isAvailable = is_available if is_available is not None else dish.isAvailable

    dish.save()

    return jsonify({'message': 'Dish updated successfully'})

# Route for deleting a dish
@app.route('/deletedish/<id>', methods=['DELETE'])
def delete_dish(id):
    dish = Dish.objects(id=id).first()

    if not dish:
        return jsonify({'message': 'Dish not found'})

    dish.delete()

    return jsonify({'message': 'Dish deleted successfully'})

# Route for retrieving all customers
@app.route('/customers', methods=['GET'])
def get_customers():
    customers = User.objects()
    customer_list = []

    for customer in customers:
        customer_data = {
            'name': customer.name,
            'email': customer.email,
            'city': customer.city,
            'wallet':customer.wallet
        }
        customer_list.append(customer_data)

    return jsonify(customer_list)

if __name__ == '__main__':
    app.run(debug=True)
