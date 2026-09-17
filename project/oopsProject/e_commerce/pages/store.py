import json


class Store:

    def __init__(self):

        self.users_file = "users.json"
        self.products_file = "products.json"
        self.carts_file = "carts.json"
        self.orders_file = "orders.json"

    def load_data(self, filename):

        try:

            with open(filename, "r") as file:

                return json.load(file)

        except FileNotFoundError:

            return []

    def save_data(self, filename, data):

        with open(filename, "w") as file:

            json.dump(
                data,
                file,
                indent=4
            )

    def get_users(self):

        return self.load_data(
            self.users_file
        )

    def get_products(self):

        return self.load_data(
            self.products_file
        )

    def get_carts(self):

        return self.load_data(
            self.carts_file
        )

    def get_orders(self):

        return self.load_data(
            self.orders_file
        )

    def save_users(self, users):

        self.save_data(
            self.users_file,
            users
        )

    def save_products(self, products):

        self.save_data(
            self.products_file,
            products
        )

    def save_carts(self, carts):

        self.save_data(
            self.carts_file,
            carts
        )

    def save_orders(self, orders):

        self.save_data(
            self.orders_file,
            orders
        )