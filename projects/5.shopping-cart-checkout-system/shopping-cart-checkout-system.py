number_of_products = int(input("Number of Products: "))


# View the shopping cart
def view_cart():
    """
    We will show the products in the cart with quantity, price, total price, discount etc.
    """

    total_product_price = product_quantity * product_price
    discount_price = 0

    promotional_discount = 10 / 100

    if total_product_price > 1000:
        discount_price = promotional_discount * total_product_price

    print(
        f"\nProduct Name: {product_name}\nQuantity: {product_quantity}\nTotal Product Price: {total_product_price}\nDiscount (10% Off if total price is greater then 1000) Price: {discount_price}\nGrand Total: {total_product_price - discount_price}\n"
    )


for num in range(1, number_of_products + 1, 1):
    product_name = input(f"Enter Product{num} Name: ")
    product_quantity = int(input("Quantity of the Product: "))
    product_price = int(input("Price of the Product: "))

    view_cart()
