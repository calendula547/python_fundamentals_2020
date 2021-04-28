def calculate_unit_price(item):
    product_price = {
        "coffee": 1.50,
        "water": 1.00,
        "coke": 1.40,
        "snacks": 2.00
    }
    for name, price in product_price.items():
        if name == item:
            return price


def calculate_total_price(item, quantity):
    unit_price = calculate_unit_price(item)
    return unit_price * quantity


product = input()
product_count = int(input())

print(f"{calculate_total_price(product, product_count):.2f}")


