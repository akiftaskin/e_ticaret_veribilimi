from product import Product
from customer import User,Customer
from cart import Cart
from order import Order

def main():
    # Ürünleri oluştur
    products = [
        Product("Laptop", 15000, 5),
        Product("Telefon", 10000, 15),
        Product("Kulaklık", 500, 150)
    ]

    # Kullanıcıdan isim ve e-posta alma
    name = input("Adınızı girin: ")
    email = input("E-posta adresinizi girin: ")
    customer = Customer(name, email)

    # Sepeti oluştur
    cart = Cart()

    while True:
        print("\n1- Ürün Ekle")
        print("2- Ürün Çıkar")
        print("3- Sepeti Görüntüle")
        print("4- Siparişi Tamamla")
        print("5- Çıkış")

        choice = input("Seçiminizi yapın: ")

        if choice == "1":
            print("\nÜrün Listesi:")
            for idx, product in enumerate(products):
                print(f"{idx + 1}. {product}")

            try:
                prod_index = int(input("Eklemek istediğiniz ürün numarasını girin: ")) - 1
                quantity = int(input("Kaç adet eklemek istiyorsunuz? "))

                if 0 <= prod_index < len(products):
                    cart.add_product(products[prod_index], quantity)
                    print(f"{products[prod_index].name} sepete eklendi.")
                else:
                    print("Geçersiz ürün numarası!")

            except ValueError:
                print("Lütfen geçerli bir sayı girin.")

        elif choice == "2":
            cart.display_cart()
            prod_name = input("Çıkarmak istediğiniz ürünün adını girin: ")
            cart.remove_product(prod_name)

        elif choice == "3":
            print("\nSepetiniz Şu Şekildedir:")
            cart.display_cart()
            

        elif choice == "4":
            order = Order(customer, cart)
            order.place_order()

        elif choice == "5":
            print("Çıkış yapılıyor...")
            break

        else:
            print("Geçersiz seçim! Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()
