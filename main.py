from product import Product
from product_manager import ProductManager
from cart import Cart

manager = ProductManager()

products = [
    Product("Smartphone", 1500, 20),
    Product("Mouse", 100, 5),
    Product("Keyboard", 150, 20)
]

for product in products:
    manager.dodavanje_proizvoda(product)

manager.prikaz_svih_proizvoda()
print(f"Ukupna vrednost svih proizvoda iznosi: {manager.ukupna_vrednost_svih_proizvoda()}")

cart = Cart()

cart.dodavanje_proizvoda_u_korpu(manager.products[0])
cart.dodavanje_proizvoda_u_korpu(manager.products[1])
cart.dodavanje_proizvoda_u_korpu(manager.products[2])

cart.prikaz_sadrzaja_korpe()
print(f"Ukupna vrednost korpe: {cart.ukupna_vrednost_korpe()}")
