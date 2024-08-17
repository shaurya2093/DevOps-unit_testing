
# E-Commerce Project Using Flask

Navigate to the specific directory
To install Flask and MongoDB use the following command 

1) pip install flask
\
After installing flask and pymongo you can simply run the below command in the terminal to start your flask application.

python app.py

## Below are the mentioned CURL command which you run in postman.

CURL Commands

1) Display Products - 
	curl --location 'http://localhost:5000/display_products'

2) Display product by ID -
	curl --location 'http://localhost:5000/display_product/1'

3) Add Products -  
	curl --location 'http://localhost:5000/add_product' \
		 --header 'Content-Type: application/json' \
		 --data '{
			"prod_id": 5, 
			"name": "Product 5", 
			"price": 40.0, 
			"description": "Amazing laptop with awesome security"
		}'

4) Get products present in the cart by user_id - 
	curl --location 'http://localhost:5000/cart/view?user_id=1234'

5) Add products to the cart by user_id - 
	curl --location 'http://localhost:5000/cart/add' \
	--header 'Content-Type: application/json' \
	--data '{
                "user_id": "1234",
                "product_id": 3,
                "quantity": 2
	        }'

6) Delete cart by user_id - 
	curl --location 'http://localhost:5000/cart/delete' \
		 --header 'Content-Type: application/json' \
		 --data '{
					"user_id": "1234",
					"product_id": 1
		        }'