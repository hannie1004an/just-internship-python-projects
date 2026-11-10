
from src.inventory.models import Product, Electronics, Clothing, Inventory


def main():
    # Create inventory
    inventory = Inventory()

    # Create electronic products
    laptop = Electronics("Laptop", 55000, 10, "HP", 2)
    smartphone = Electronics("Smartphone", 25000, 15, "Samsung", 1)

    # Create clothing products
    shirt = Clothing("Shirt", 800, 20, "M", "Cotton")
    jeans = Clothing("Jeans", 1500, 12, "L", "Denim")

    # Add products to inventory
    inventory.add_product(laptop)
    inventory.add_product(smartphone)
    inventory.add_product(shirt)
    inventory.add_product(jeans)

    # Display inventory
    print("=" * 50)
    print("       INVENTORY MANAGEMENT SYSTEM")
    print("=" * 50)

    print(inventory)
    print("\nPRODUCT DETAILS")
    print("-" * 50)

    inventory.display_products()

    print("\nDEVELOPER REPRESENTATION")
    print("-" * 50)
    print(repr(inventory))


if __name__ == "__main__":
    main()
