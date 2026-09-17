class Order:

    def __init__(
        self,
        order_id,
        user_id,
        items,
        total
    ):

        self.order_id = order_id
        self.user_id = user_id
        self.items = items
        self.total = total
        self.status = "Placed"

    def get_order_details(self):

        return {
            "order_id": self.order_id,
            "user_id": self.user_id,
            "items": self.items,
            "total": self.total,
            "status": self.status
        }

    def cancel_order(self):

        self.status = "Cancelled"