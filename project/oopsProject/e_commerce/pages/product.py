class Product:

    def __init__(
        self,
        product_id,
        name,
        price,
        category,
        stock
    ):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.category = category
        self.stock = stock

    def display_product(self):

        return {
            "id": self.product_id,
            "name": self.name,
            "price": self.price,
            "category": self.category,
            "stock": self.stock
        }

    def reduce_stock(self, quantity):

        if quantity <= self.stock:

            self.stock -= quantity

            return True

        return False