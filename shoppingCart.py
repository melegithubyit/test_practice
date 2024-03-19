class ShoppingCart:
    def __init__(self):
        self.products = []
    def addProduct(self, product):
        self.products.append(product)
    def calculateTotal(self):
        total = 0
        for p in self.products:
            total += p.calcuateTotal()
        return total