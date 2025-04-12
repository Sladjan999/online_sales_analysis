from product import Product
from product_manager import ProductManager
from cart import Cart

manager = ProductManager()

products = [
    Product("Laptop", 1500, 10),
    Product("Tablet", 100, 22),
    Product("Speakers", 150, 6)
]

for product in products:
    manager.dodavanje_proizvoda(product)

cart = Cart()

cart.dodavanje_proizvoda_u_korpu(manager.products[0])
cart.dodavanje_proizvoda_u_korpu(manager.products[1])
cart.dodavanje_proizvoda_u_korpu(manager.products[2])

cart.prikaz_sadrzaja_korpe()
print(f"Ukupna vrednost korpe: {cart.ukupna_vrednost_korpe()}")
