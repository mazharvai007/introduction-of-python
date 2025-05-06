# Enter number of products
number_of_products = int(input("Enter number of sales item: "))


def sales_summery():
    total_unit_price = product_quantity * per_unit_price
    print(
        f"\nProduct Name: {product_name}\nQuantity: {product_quantity}\nPer Unit Price: {per_unit_price}\nTotal Revenue: {total_unit_price}\n"
    )


# Control number of products
for num in range(1, number_of_products + 1, 1):
    product_name = input(f"Enter Product{num} Name: ")
    product_quantity = int(input("Quantity of the product: "))
    per_unit_price = int(input("Price per unit: "))

    sales_summery()
