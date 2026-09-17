class User:

    def __init__(self, user_id, name, email, password, role):
        self.user_id = user_id
        self.name = name
        self.email = email
        self.password = password
        self.role = role

    def login(self, email, password):

        if self.email == email and self.password == password:
            return True

        return False

    def get_details(self):

        return {
            "id": self.user_id,
            "name": self.name,
            "email": self.email,
            "role": self.role
        }


class Customer(User):

    def dashboard(self):

        return "Customer Dashboard"


class Admin(User):

    def dashboard(self):

        return "Admin Dashboard"