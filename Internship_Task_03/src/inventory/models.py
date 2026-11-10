
class Product:
    """Base class representing a product in the inventory."""

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # Name property
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Product name cannot be empty.")
        self.__name = value

    # Price property
    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price must be greater than zero.")
        self.__price = value

    # Quantity property
    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if not isinstance(value, int) or isinstance(value, bool) or value < 0:
            raise ValueError("Quantity must be a non-negative integer.")
        self.__quantity = value

    # Magic methods
    def __str__(self):
        return f"{self.name} - Rs.{self.price} - Stock: {self.quantity}"

    def __repr__(self):
        return (
            f"Product(name={self.name!r}, "
            f"price={self.price!r}, quantity={self.quantity!r})"
        )
    
class Electronics(Product):
    """Child class representing electronic products."""

    def __init__(self, name, price, quantity, brand, warranty_years):
        super().__init__(name, price, quantity)
        self.brand = brand
        self.warranty_years = warranty_years

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, value):
        if not value:
            raise ValueError("Brand cannot be empty.")
        self.__brand = value

    @property
    def warranty_years(self):
        return self.__warranty_years

    @warranty_years.setter
    def warranty_years(self, value):
        if not isinstance(value, int) or isinstance(value, bool) or value < 0:
            raise ValueError("Warranty must be a non-negative integer.")
        self.__warranty_years = value

    def __str__(self):
        return (
            f"{self.name} - {self.brand} - "
            f"Rs.{self.price} - Warranty: {self.warranty_years} years"
        )
    
    def __repr__(self):
        return (
            f"Electronics(name={self.name!r}, "
            f"price={self.price!r}, quantity={self.quantity!r}, "
            f"brand={self.brand!r}, "
            f"warranty_years={self.warranty_years!r})"
        )

    
class Clothing(Product):
    """Child class representing clothing products."""

    def __init__(self, name, price, quantity, size, material):
        super().__init__(name, price, quantity)
        self.size = size
        self.material = material

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        allowed_sizes = ["S", "M", "L", "XL", "XXL"]

        if value not in allowed_sizes:
            raise ValueError("Invalid clothing size.")
        self.__size = value

    @property
    def material(self):
        return self.__material

    @material.setter
    def material(self, value):
        if not value:
            raise ValueError("Material cannot be empty.")
        self.__material = value

    def __str__(self):
        return (
            f"{self.name} - Size: {self.size} - "
            f"Material: {self.material} - "
            f"Rs.{self.price} - Stock: {self.quantity}"
        )
    
    def __repr__(self):
        return (
            f"Clothing(name={self.name!r}, "
            f"price={self.price!r}, quantity={self.quantity!r}, "
            f"size={self.size!r}, material={self.material!r})"
        )

    
class Inventory:
    """Class for managing inventory products."""

    def __init__(self):
        self.products = []

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Only Product objects can be added.")
        self.products.append(product)

    def display_products(self):
        for product in self.products:
            print(product)

    def __str__(self):
        return f"Inventory contains {len(self.products)} products."

    def __repr__(self):
        return f"Inventory(products={self.products!r})"



