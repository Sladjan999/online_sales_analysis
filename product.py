class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def prikaz_informacija_za_proizvode(self):
         print(f"Ime proizvoda: {self.name}, Cena proizvoda: {self.price}, Kolicina proizvoda: {self.quantity}")
    
    def azuriranje_kolicine_proizvoda(self, quantity):
        if quantity < 0 :
            print("Kolicina proizvoda ne moze biti manja od 1")
        else:
            self.quantity = quantity
            print(f"Azurirana kolicina proizvoda za korisnika: {self.name}, iznosi: {self.quantity}")