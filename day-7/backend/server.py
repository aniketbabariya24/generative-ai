from flask import Flask, request, jsonify
from mongoengine import connect, Document, StringField, FloatField, IntField, BooleanField, ReferenceField, ListField
from dotenv import load_dotenv
from flask_socketio import SocketIO, emit
from flask_bcrypt import Bcrypt
import jwt
from bson import json_util
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
    cart = ListField(ReferenceField('Dish'))
    wallet = FloatField(default=0)

# Schema for Dishes
class Dish(Document):
    name = StringField(required=True)
    description = StringField(required=True)
    image = StringField(required=True)
    price = FloatField(required=True)
    stocks = IntField(required=True)
    quantity = IntField(default=0)
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
    cart = request.json.get('cart')
    wallet = request.json.get('wallet')

    # Create a new user
    user = User(name=name, email=email, cart=cart, password=password, city=city, wallet=wallet)
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
    image = request.json.get('image')
    price = request.json.get('price')
    stocks = request.json.get('stocks')
    quantity = request.json.get('quantity')
    is_available = request.json.get('isAvailable', True)

    # Create a new dish
    dish = Dish(name=name , description=description, quantity=quantity ,image=image, price=price, stocks=stocks, isAvailable=is_available)
    dish.save()

    return jsonify({'message': 'Dish added successfully'})

# Route for retrieving all dishes
@app.route('/dishes', methods=['GET'])
def get_dishes():
    dishes = Dish.objects()
    dish_list = []

    for dish in dishes:
        dish_data = {
            'id':str(dish.id),
            'name': dish.name,
            'price': dish.price,
            'stocks': dish.stocks,
            'quantity': dish.quantity,
            'description':dish.description,
            'image':dish.image,
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
    quantity = request.json.get('quantity')
    description = request.json.get('description')
    image = request.json.get('image')
    is_available = request.json.get('isAvailable')

    dish.name = name if name else dish.name
    dish.price = price if price else dish.price
    dish.stocks = stocks if stocks else dish.stocks
    dish.quantity = quantity if quantity else dish.quantity
    dish.description = description if description else dish.description
    dish.image = image if image else dish.image
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

@app.route('/deletec/<id>', methods=['DELETE'])
def delete_customer(id):
    user = User.objects(id=id).first()

    if not user:
        return jsonify({'message': 'User not found'})

    user.delete()

    return jsonify({'message': 'User deleted successfully'})


@app.route('/customer/<id>', methods=['GET'])
def get_customer(id):
    # Find the customer by ID
    customer = User.objects(id=id).first()
    
    if not customer:
        return jsonify({'message': 'Customer not found'}), 404
    
    cart_data = [item.to_mongo() for item in customer.cart]

    # Prepare the customer data
    customer_data = {
        'id':str(customer.id),
            'name': customer.name,
            'email': customer.email,
            'city': customer.city,
            'cart':  json_util.dumps(cart_data),
            'wallet':customer.wallet
    }

    return jsonify(customer_data), 200

@app.route('/dish/<id>', methods=['GET'])
def get_dish(id):
    # Find the customer by ID
    dish = Dish.objects(id=id).first()
    
    if not dish:
        return jsonify({'message': 'dish not found'}), 404

    # Prepare the dish data
    dish_data = {
            'id':str(dish.id),
            'name': dish.name,
            'price': dish.price,
            'stocks': dish.stocks,
            'quantity': dish.quantity,
            'description':dish.description,
            'image':dish.image,
            'isAvailable': dish.isAvailable
        }

    return jsonify(dish_data), 200


# Route for retrieving all customers
@app.route('/customers', methods=['GET'])
def get_customers():
    customers = User.objects()
    customer_list = []

    for customer in customers:
        cart_data = [item.to_mongo() for item in customer.cart]
        customer_data = {
            'id':str(customer.id),
            'name': customer.name,
            'email': customer.email,
            'city': customer.city,
            'cart':  json_util.dumps(cart_data),
            'wallet':customer.wallet
        }
        customer_list.append(customer_data)

    return jsonify(customer_list)

@app.route('/addtocart/<id>/<did>', methods=['POST'])
def add_to_cart(id,did):
   
    data = request.get_json()
  
    user = User.objects.get(id=id)
    dish = Dish.objects.get(id=did)

    user.cart.append(dish)
    user.save()

    return jsonify({'message': 'Dish added to cart successfully'})


if __name__ == '__main__':
    app.run(debug=True)
