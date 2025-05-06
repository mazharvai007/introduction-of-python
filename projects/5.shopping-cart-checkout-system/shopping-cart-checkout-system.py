number_of_products = int(input("Number of products: "))


def view_cart():
    total_product_price = product_quantity * product_price
    discount_price = 0

    promotional_discount = 10 / 100

    if total_product_price > 1000:
        discount_price = promotional_discount * total_product_price

    return f"\nProduct Name: {product_name}\nQuantity: {product_quantity}\nTotal Product Price: {total_product_price}\nDiscount (10% Off if total price is greater then 1000) Price: {discount_price}\nGrand Total: {total_product_price - discount_price}\n"


def check_value(get_value: int, topic_name: str):
    """
    We are checking integer value
    """

    if not (get_value > 0):
        print(
            f"You entered invalid value {get_value} for {topic_name}. You must enter integer value"
        )
        return int(input(f"Enter value for {topic_name}: "))
    return get_value


for num in range(1, number_of_products + 1, 1):
    product_name = input(f"Enter product {num} name: ")
    product_quantity = check_value(int(input("Quantity of the product: ")), "Quantity")
    product_price = check_value(int(input("Price of the product: ")), "Price")

    print(view_cart())
