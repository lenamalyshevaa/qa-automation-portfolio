

class Inventory():
    def __init__(self):
        self.products = {}

    def add(self, item, qty):
        self.products[item] = self.products.get(item, 0) + qty

    def remove(self, item, qty):
        if (self.products.get(item, 0)) < qty:
            raise ValueError('Недостаточное кол-во в наличии')    
        self.products[item] = self.products.get(item, 0) - qty
        if self.products[item] == 0: 
            self.products.pop(item, None) 

    def count(self, item):
        return self.products.get(item, 0)

    def total(self):
        result = sum(self.products.values())
        return result