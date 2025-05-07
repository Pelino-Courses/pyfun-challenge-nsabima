class product:
    """
    represent a product in inventory system.
    Attributes:
    name is the name of product.
    price is the price per unit of product
    quantity is the quantity of product in stock.
    """
    def __init__(self,name,price,quantity):
        """
        initilize a new product with instance ,name,price and quantity.
        Raise:
            ValueError: if price or quantity is negative
            """
        if price < 0:
            raise ValueError("price can not be negative")
        if quantity < 0:
            raise ValueError("quantity can not be negative")
        self.name = name
        self.price = price
        self.quantity = quantity
    def add_inventory(self, amount):
        """
        Add stock to the product inventory.
        Args:
            amount : number of items to add must be positive
        Raise:
             ValueError: if amount is negative.
        """
        if amount < 0:
            raise ValueError("amount to add must be a postive")
        self.quantity +=amount
        def remove_inventory(self,amount):
            """
            removes stock from product inventory.
            Args: amount to be removed 
            Raises:
                 ValueError: if amount is not valid.
            """
            if amount < 0:
                raise ValueError("amount to remove is negative")
            self.quantity -= amount
            def tatol_value(self) -> float:
                """calculate the tatol value of the proct in stock.
                   returns:
                     tatol value'
                     """
                return self.price * self.quantity
            def display_info(self) -> str:
                """
                returns a formtted string containg product detail.
                returns:
                       decription of the product, including name, price
                       """
                return (
                    f"product : {self.name}\n"
                    f"price : {self.price}\n"
                    f"quantity : {self.quantity}\n"
                    f"tatol value : {self.tatol_value}"
                )
                


