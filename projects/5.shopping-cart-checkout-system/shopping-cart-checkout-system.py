number_of_products = int(input("Number of products: "))

for value in range(1, number_of_products + 1):
    product_name = input(f"Enter product {value} name: ")
    product_quantity = int(input("Quantity of the product: "))
    product_price = int(input("Price of the product: "))


def view_cart():
    total_product_price = product_quantity * product_price
    discount_price = 0

    promotional_discount = 10 / 100

    if total_product_price > 1000:
        discount_price = promotional_discount * total_product_price

    print(discount_price)

    return f"\nProduct Name: {product_name}\nQuantity: {product_quantity}\nTotal Product Price: {total_product_price}\nDiscount (10% Off if total price is greater then 1000) Price: {discount_price}\nGrand Total: {total_product_price - discount_price}"


print(view_cart())
