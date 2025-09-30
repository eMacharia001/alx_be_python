class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity
    
product1 = Product("Laptop", 750, 5)
product2 = Product("iphone", 1000, 12)

print(f"{product1.name} Stock Value: ${product1.total_value()}")
print(f"{product2.name} Stock Value: ${product1.total_value()}")
