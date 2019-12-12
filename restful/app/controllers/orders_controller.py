class OrdersController(object):
    def __init__(self, orders_service):
        self.__orders_service = orders_service

    def get_orders(self, number_of_items=5, timestamp=None):
        #Validate the user request/input - validated the value are legal/exist
        #Transform the service request

        orders =  self.__orders_service.get_orders(number_of_items, timestamp)
        return orders_response = {'orders': [order.__dict__ for order in orders]}
