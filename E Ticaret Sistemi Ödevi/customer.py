class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Customer(User):
    def __init__(self, name, email):
        super().__init__(name, email)

    def __str__(self):
        return f"Müşteri: {self.name}, E-posta: {self.email}"
