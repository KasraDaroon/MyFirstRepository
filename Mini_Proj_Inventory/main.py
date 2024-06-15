class Product:

    products = []

    def __init__(self, name, price, quantity):

        self.name = name

        self.price = price

        self.quantity = quantity

        Product.products.append(self)

    def display_info(self):

        print(f"name: {self.name}")

        print(f"price: ${self.price}")

        print(f"quantity: {self.quantity}")

    def update_quantity(self, amount):

        self.quantity += amount

    def calculate_total_value(self):

        total_value = 0

        for product in Product.products:

            total_value += product.price * product.quantity

        return total_value
    