class Order:
    def __init__(self, customer, cart):
        self.customer = customer
        self.cart = cart
        self.total_amount = cart.get_amount()

    def place_order(self):
        if self.total_amount > 0:
            print("\nSiparişiniz başarılı bir şekilde oluşturuldu.")
            print(self.customer)
            print("\nSipariş detayları:")
            self.cart.display_cart()
            print(f"\nToplam Tutar: {self.total_amount} TL")
        else:
            print("\nSepet boş, sipariş oluşturulamadı.")
