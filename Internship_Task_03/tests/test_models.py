
import pytest

from src.inventory.models import Product, Electronics, Clothing, Inventory


def test_product_creation():
    product = Product("Laptop", 50000, 10)

    assert product.name == "Laptop"
    assert product.price == 50000
    assert product.quantity == 10


def test_electronics_inheritance():
    laptop = Electronics("Laptop", 50000, 5, "HP", 2)

    assert isinstance(laptop, Product)
    assert laptop.brand == "HP"
    assert laptop.warranty_years == 2


def test_clothing_inheritance():
    shirt = Clothing("Shirt", 800, 20, "M", "Cotton")

    assert isinstance(shirt, Product)
    assert shirt.size == "M"
    assert shirt.material == "Cotton"


def test_inventory_add_product():
    inventory = Inventory()
    product = Product("Mouse", 500, 15)

    inventory.add_product(product)

    assert len(inventory.products) == 1
    assert inventory.products[0].name == "Mouse"

def test_product_price_setter():
    product = Product("Keyboard", 1000, 10)

    product.price = 1500

    assert product.price == 1500

    with pytest.raises(ValueError):
        product.price = -100


def test_product_quantity_setter():
    product = Product("Mouse", 500, 10)

    product.quantity = 20

    assert product.quantity == 20

    with pytest.raises(ValueError):
        product.quantity = -5


def test_electronics_warranty_setter():
    laptop = Electronics("Laptop", 50000, 5, "HP", 2)

    laptop.warranty_years = 3

    assert laptop.warranty_years == 3

    with pytest.raises(ValueError):
        laptop.warranty_years = -1


def test_clothing_size_setter():
    shirt = Clothing("Shirt", 800, 20, "M", "Cotton")

    shirt.size = "L"

    assert shirt.size == "L"

    with pytest.raises(ValueError):
        shirt.size = "INVALID"

        
def test_product_str_method():
    product = Product("Laptop", 50000, 10)

    result = str(product)

    assert "Laptop" in result
    assert "50000" in result
    assert "10" in result


def test_product_repr_method():
    product = Product("Laptop", 50000, 10)

    result = repr(product)

    assert "Product" in result
    assert "Laptop" in result


def test_electronics_str_override():
    laptop = Electronics("Laptop", 50000, 5, "HP", 2)

    result = str(laptop)

    assert "HP" in result
    assert "Warranty" in result


def test_inventory_repr_method():
    inventory = Inventory()
    inventory.add_product(Product("Mouse", 500, 10))

    result = repr(inventory)

    assert "Inventory" in result
    assert "Mouse" in result
    
def test_clothing_repr_method():
    shirt = Clothing("Shirt", 800, 20, "M", "Cotton")

    result = repr(shirt)

    assert "Clothing" in result
    assert "Cotton" in result


def test_inventory_rejects_invalid_object():
    inventory = Inventory()

    with pytest.raises(TypeError):
        inventory.add_product("Laptop")


