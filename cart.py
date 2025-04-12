class Cart:
    def __init__(self):
        self.cart_items = []

    def dodavanje_proizvoda_u_korpu(self, product):
        self.cart_items.append(product)

    def prikaz_sadrzaja_korpe(self):
        for item in self.cart_items:
            item.prikaz_informacija_za_proizvode()

    def ukupna_vrednost_korpe(self):
        return sum(item.price * item.quantity for item in self.cart_items)
