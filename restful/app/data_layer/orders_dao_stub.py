from app.data_layer.entities.order_record import OrderRecord

ORDERS = [
    OrderRecord(10, 24, 0),
    OrderRecord(20, 24, 1),
    OrderRecord(30, 24, 2),
    OrderRecord(40, 24, 3),
    OrderRecord(50, 24, 4),
    OrderRecord(60, 24, 5),
    OrderRecord(70, 24, 6),
        
]

class OrdersDaoStub(object):
    #Should implement CRUD of the database table
    # reaseon for the params (fitering) so the dal layer is not wasteful
    def get_orders(self, number_of_items, index=None):
        return ORDERS
