class Product:
    def __init__(self, product_type, name, price):
        self.type = product_type
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self):
        self.products = {}
        self.income = 0  

    def add(self, product, amount):
        if not isinstance(product, Product):
            raise ValueError("Invalid product. Please provide a valid Product instance.")

        if product in self.products:
            self.products[product] += amount
        else:
            self.products[product] = amount

    def set_discount(self, identifier, percent, identifier_type='name'):
        if identifier_type not in ('type', 'name'):
            raise ValueError("Invalid identifier_type. Please choose 'type' or 'name'.")

        for product in self.products:
            if (identifier_type == 'type' and product.type == identifier) or (
                    identifier_type == 'name' and product.name == identifier):
                product.price *= (1 - percent / 100)

    def sell_product(self, product_name, amount):
        for product, stock in self.products.items():
            if product.name == product_name:
                if stock >= amount:
                    product_total_price = product.price * amount
                    self.income += product_total_price
                    self.products[product] -= amount
                    return
                else:
                    raise ValueError("Not enough stock available to sell.")

        raise ValueError(f"Product '{product_name}' not found in the store.")

    def get_income(self):
        return self.income

    def get_all_products(self):
        return [(product.name, self.products[product]) for product in self.products]

    def get_product_info(self, product_name):
        for product, stock in self.products.items():
            if product.name == product_name:
                return (product.name, stock)

        raise ValueError(f"Product '{product_name}' not found in the store.")


# Test the implementation
p = Product('Sport', 'Football T-Shirt', 100)
p2 = Product('Food', 'Ramen', 1.5)
s = ProductStore()

s.add(p, 10)
s.add(p2, 300)
s.sell_product('Ramen', 10)

print(s.get_product_info('Ramen'))  # Output: ('Ramen', 290)
