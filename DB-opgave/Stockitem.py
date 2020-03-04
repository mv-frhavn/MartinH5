from Article import Article


class StockItem(Article):  # inherit from Article class (and by that also the DBclass)
    def __init__(self, article_id, name, description, stock_item_id, quantity, location):
        super().__init__(article_id, name, description)
        self.stock_item_id = stock_item_id
        self.quantity = quantity
        self.location = location

    def new_item(self):  # method overriding article.new_item, used to create a new stock item, with Location
        try:
            query = """
            INSERT INTO [Stockitem] ([Stockitem_Id], [Quantity], [Article_Id], [Location_Id])
            VALUES ('{0}', '{1}', '{2}', '{3}');
            """.format(self.stock_item_id, self.quantity, self.article_id, self.location.location_id)
            self.terminal(query)

        except:
            return False

    def rem_item(self):  # Simply looks for the Stock_item_id in the DB and removes that row
        try:
            query = """
            DELETE FROM [Stockitem] WHERE [Stockitem_Id] = {0};
            """.format(self.stock_item_id)
            self.terminal(query)

        except:
            return False

    def inc_quant(self):  # Used to increase the quantity of an item, should be used together with the Location.new_item
        try:
            query = """
            update [Stockitem] 
            set Quantity = Quantity + 1 
            where [Stockitem_Id] = {0}
            """.format(self.stock_item_id)
            self.terminal(query)

        except:
            return False

    def dec_quant(self):  # Same as the class before, but decrease the quantity
        try:
            query = """
            update [Stockitem] 
            set Quantity = Quantity - 1 
            where [Stockitem_Id] = {0}
            """.format(self.stock_item_id)
            self.terminal(query)

        except:
            return False

