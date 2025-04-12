from product import Product

class ProductManager:
    def __init__(self):
        self.products =[]
        
    def dodavanje_proizvoda(self, product):
        self.products.append(product)
    
    def prikaz_svih_proizvoda(self):
        for product in self.products:
            product.prikaz_informacija_za_proizvode()

    def ukupna_vrednost_svih_proizvoda(self):
        return sum(p.price * p.quantity for p in self.products)
    
    def uklanjanje_proizvoda_po_imenu(self, name):
        self.products = [p for p in self.products if p.name != name]