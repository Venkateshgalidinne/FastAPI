class Cart:

    def __init__(self, user_id):

        self.user_id = user_id
        self.items = []

    def add_product(self, product, quantity):

        if quantity <= product.stock:

            item = {
                "product_id": product.product_id,
                "name": product.name,
                "price": product.price,
                "quantity": quantity
            }

            self.items.append(item)

            return True

        return False

    def remove_product(self, product_id):

        self.items = [
            item
            for item in self.items
            if item["product_id"] != product_id
        ]

    def calculate_total(self):

        total = 0

        for item in self.items:

            total += item["price"] * item["quantity"]

        return total

    def clear_cart(self):

        self.items = []