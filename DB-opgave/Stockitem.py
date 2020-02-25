class StockItem:
    def __init__(self, stock_item_id, item_number, weight, quantity, article_id, location_id):
        self.stock_item_id = stock_item_id
        self.item_number = item_number
        self.weight = weight
        self.quantity = quantity
        self.article_id = article_id
        self.location_id = location_id


class NewItem(StockItem):
    pass


class RemoveItem(StockItem):
    pass


class IncQuantity(StockItem):
    pass


class DecQuantity(StockItem):
    pass


