class Sale:
    def __init__(self, item_name, quantity, price_per_item):
        self.item_name = item_name
        self.quantity = quantity
        self.price_per_item = price_per_item

    def calculate_total(self):
        return self.quantity * self.price_per_item

    def apply_discount(self, discount):
        total = self.calculate_total()
        discounted_total = total * (1 - discount / 100)
        return discounted_total

    def display_sale_info(self):
        print (f"Item: {self.item_name}")
        print (f"Quantity: {self.quantity}")
        print (f"Price Per Item: ${self.price_per_item:.2f}")
        print (f"Total Cost: ${self.calculate_total():.2f}")

# Example Usage 
sale = Sale("Laptop", 2, 1500.00)

# Display Sales Information 
sale.display_sale_info()

# Calculate the total cost of sale
total_cost = sale.calculate_total()
print (f"Total cost before discount: ${total_cost:.2f}")

# Apply a 10% discount
discounted_cost = sale.apply_discount(10)
print (f"Total cost after 10% discount: ${discounted_cost:.2f}")