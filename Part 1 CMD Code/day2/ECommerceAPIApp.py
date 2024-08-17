from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Temporary Product data
products = [
    {
        'id' : 1,
        'name': 'laptop',
        'price': 45.80,
        'description':'HP Laptop with 8GB RAM and 1 TB HDD'
        
    }
] 

#Temp cart data 
carts = {}

# Routes for handling differnt API endpoints
@app.route('/display_products', methods=['GET'])
def get_products():
    return jsonify(products)   
    
from flask import request, jsonify

@app.route('/cart/add', methods=['GET'])
def add_to_cart():
    data = request.get_json()
    user_id= data.get('user_id')
    product_id = data.get('product_id')
    quantity = data.get('quantity', 1)
    
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return jsonify({'error': 'product not found'}), 404
        
    #Add the product to the user's cart or update the quantity if item already in the cart
    cart = carts.get(user_id, {})
    cart[product_id] = cart.get(product_id, 0) + quantity 
    carts[user_id] = cart
    print(cart)
    print(carts)
    
    return jsonify(cart)

print(carts)
if __name__ == '__main__':
        app.run(debug=True)


