from product import Product

if __name__ == "__main__":
    try:
        product = Product("Laptop", 1200.50, 10)
        print(product.display_info())

        product.add_inventory(5)
        print("After adding inventory:", product.display_info())

        product.remove_inventory(3)
        print("After removing inventory:", product.display_info())

        print("Total value of inventory:", product.total_value())
    except Exception as e:
        print(f"Error: {e}")
def total_value(self)->float:
        """"
        calculate the total value of current stock
        """
        return self.price*self.quantity
    def display(self):
        """"
        prints out my product details
        """
        print(f"product name:{self.name}")
        print(f"price:{self.price}")
        print(f"quantity:{self.quantity}")
        print(f"total invetory value:{self.total_value():.2f}") 
        
        
        
class inventory:
    def __init__(self):
        # self.name = name
        self.inventory = []
        # self.price = price
        # self.quantity = quantity
    def add_product(self,product:product):
        self.inventory.append(product)
    def remove_product(self, id):
        ind =  0
        for i in self.inventory:
            if(i.id == id):
                del self.inventory[ind]
                print(i, "Deleted successfully!")
                break
            ind += 1
    def show_products(self):
        for product in self.inventory:
            print(product)
    
invent = inventory()

id = randint(0, 2000)
# id = int(input("Enter product id: "))
name = input("Please enter the name of the product: ")
price = int(input("enter the price: "))
qty = int(input("enter the quantity: "))
products = [
    product(id, name, price, qty),
    product(1, "pants", 5000, 3),
    product(2, "shirt", 532, 3),
    product(3, "phone", 788, 3),
    product(4, "vehicle", 5000, 3),
    ]
for i in products:
    invent.add_product(i)
invent.show_products()
invent.remove_product(4)
invent.show_products()
