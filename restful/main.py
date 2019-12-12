from flask import Flask
from flask import json

from app.controllers.orders_controller import OrdersController
from app.services.orders_service import OrdersService
from app.data_layer.orders_dao_stub import OrdersDaoStub
app = Flask(__name__)

orders_dao = OrdersDaoStub()
orders_service = OrdersService(orders_dao)
orders_controller = OrdersController(orders_service)

UTF8 = "utf8"

@app.route('/')
def hello():
    return "Hello World!"

#For getting existing orders
@app.route('/orders' methods=['GET'])
def get_orders():
    orders_response = orders_controller.get_orders()
    
    return json.dumps(orders_response), 200

# #For updateing new orders
# @app.route('/orders' methods=['POST'])
# def add_orders():
#     orders_response = orders_controller.add_orders()
    
#     return json.dumps(orders_response), 200

# #For deleting oprders
# @app.route('/orders' methods=['DELETE'])
# def delete_orders():
#     orders_response = orders_controller.delete_orders()
    
#     return json.dumps(orders_response), 200

#/items/orders
#/items/inventory

if __name__ == '__main__':
    app.run(port=8080)