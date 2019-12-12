class OrdersService(object):
    def __init__(self, orders_dao):
        self.__orders_dao = orders_dao

    def get_orders(self, number_of_items, index=None):
        # Should take care of the bussiness logic
        return self.__orders_dao.get_orders(number_of_items, index)