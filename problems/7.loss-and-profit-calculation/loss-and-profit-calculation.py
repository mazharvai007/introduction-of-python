# Name of cakes
black_forest = "Black Forest"
vanilla = "Vanilla"
red_velvet = "Red Velvet"
lemon_sponge = "Lemon Sponge"
chocolate = "Chocolate"

# Cakes inventory costs
black_forest_material_costs = 180
vanilla_material_costs = 150
red_velvet_material_costs = 220
lemon_sponge_material_costs = 165
chocolate_material_costs = 170

# Transportation costs
transportation_costs_each_pound = 150

# Utility costs
# utility_costs_each_pound = 3 / 100

# Space costs
space_costs_each_pound = 50

# Stuff costs
stuff_costs_each_pound = 60

# Cakes selling price
black_forest_selling_price = 780
vanilla_selling_price = 600
red_velvet_selling_price = 800
lemon_sponge_selling_price = 650
chocolate_selling_price = 660

# Discount
five_percent_discount = 5 / 100
seven_percent_discount = 7 / 100

# Sales after discount
black_forest_sales = 5
vanilla_sales = 7
red_velvet_sales = 10
lemon_sponge_sales = 5
chocolaet_sales = 9

# Solutions

# Owner wants to visualize the each cake flavor types

cake_list = [black_forest, vanilla, red_velvet, lemon_sponge, chocolate]
print(f"List of Cakes: {cake_list}")

# Owner wants to visualize the total inventory costs for each cake per pound

# Add transportation costs with material costs
black_forest_material_transport_costs = (
    black_forest_material_costs + transportation_costs_each_pound
)
vanilla_material_transport_costs = (
    vanilla_material_costs + transportation_costs_each_pound
)
red_velvet_material_transport_costs = (
    red_velvet_material_costs + transportation_costs_each_pound
)
lemon_sponge_material_transport_costs = (
    lemon_sponge_material_costs + transportation_costs_each_pound
)
chocolate_material_transport_costs = (
    chocolate_material_costs + transportation_costs_each_pound
)

print(
    f"Material with Transportation costs: {black_forest_material_transport_costs} {vanilla_material_transport_costs} {red_velvet_material_transport_costs} {lemon_sponge_material_transport_costs} {chocolate_material_transport_costs}"
)

# Get 3% utility costs based on each cake material and transportation cost
black_forest_utility_costs = (black_forest_material_transport_costs * 3) / 100
vanilla_utility_costs = (vanilla_material_transport_costs * 3) / 100
red_velvet_utility_costs = (red_velvet_material_transport_costs * 3) / 100
lemon_sponge_utility_costs = (lemon_sponge_material_transport_costs * 3) / 100
chocolate_utility_costs = (chocolate_material_transport_costs * 3) / 100

print(
    f"Get 3 percent utility costs: {black_forest_utility_costs} {vanilla_utility_costs} {red_velvet_utility_costs} {lemon_sponge_utility_costs} {chocolate_utility_costs}"
)

# Add Utility Costs with material and trasportation cost
black_forest_utility_costs_add = (
    black_forest_material_transport_costs + black_forest_utility_costs
)
vanilla_utility_costs_add = vanilla_material_transport_costs + vanilla_utility_costs
red_velvet_utility_costs_add = (
    red_velvet_material_transport_costs + red_velvet_utility_costs
)
lemon_sponge_utility_costs_add = (
    lemon_sponge_material_transport_costs + lemon_sponge_utility_costs
)
chocolate_utility_costs_add = (
    chocolate_material_transport_costs + chocolate_utility_costs
)

print(
    f"Costs with Utility: {black_forest_utility_costs_add} {vanilla_utility_costs_add} {red_velvet_utility_costs_add} {lemon_sponge_utility_costs_add} {chocolate_utility_costs_add}"
)

# Add space and stuff costs
black_forest_inventory_total_costs = (
    black_forest_utility_costs_add + space_costs_each_pound + stuff_costs_each_pound
)
vanilla_inventory_total_costs = (
    vanilla_utility_costs_add + space_costs_each_pound + stuff_costs_each_pound
)
red_velvet_inventory_total_costs = (
    red_velvet_utility_costs_add + space_costs_each_pound + stuff_costs_each_pound
)
lemon_sponge_inventory_total_costs = (
    lemon_sponge_utility_costs_add + space_costs_each_pound + stuff_costs_each_pound
)
chocolate_inventory_total_costs = (
    chocolate_utility_costs_add + space_costs_each_pound + stuff_costs_each_pound
)

print(
    f"Add space and stuff costs: {black_forest_inventory_total_costs} {vanilla_inventory_total_costs} {red_velvet_inventory_total_costs} {lemon_sponge_inventory_total_costs} {chocolate_inventory_total_costs}"
)

# Total Inventory Costs
total_inventory_costs = (
    black_forest_inventory_total_costs
    + vanilla_inventory_total_costs
    + red_velvet_inventory_total_costs
    + lemon_sponge_inventory_total_costs
    + chocolate_inventory_total_costs
)
print(f"Total Inventory costs: {total_inventory_costs.__round__(2)}")

# Owner wants to visualize the selling price before discount for each cake per pound

selling_price_before_discount = (
    black_forest_selling_price
    + vanilla_selling_price
    + red_velvet_selling_price
    + lemon_sponge_selling_price
    + chocolate_selling_price
)
print(f"Total Selling Price Before Discount: {selling_price_before_discount}")

print(
    f"Selling Price Before Discount: {black_forest_selling_price} {vanilla_selling_price} {red_velvet_selling_price} {lemon_sponge_selling_price} {chocolate_selling_price}"
)

# Owner wants to visualize the selling price after discount for each cake per pound

# 5% discount for first 3 types of cake
black_forest_five_percent_discount_price = (black_forest_selling_price * 5) / 100
vanilla_five_percent_discount_price = (vanilla_selling_price * 5) / 100
red_velvet_five_percent_discount_price = (red_velvet_selling_price * 5) / 100

print(
    f"Get 5 percent discount over selling price: {black_forest_five_percent_discount_price} {vanilla_five_percent_discount_price} {red_velvet_five_percent_discount_price}"
)

# 7% discount for rest types of cake
lemon_sponge_seven_percent_discount_price = (lemon_sponge_selling_price * 7) / 100
chocolate_seven_percent_discount_price = (chocolate_selling_price * 7) / 100

print(
    f"Get 7 percent discount over selling price {lemon_sponge_seven_percent_discount_price} {chocolate_seven_percent_discount_price}"
)

# Get selling price after discount
black_forest_discount_selling_price = (
    black_forest_selling_price - black_forest_five_percent_discount_price
)
vanilla_discount_selling_price = (
    vanilla_selling_price - vanilla_five_percent_discount_price
)
red_velvet_discount_selling_price = (
    red_velvet_selling_price - red_velvet_five_percent_discount_price
)
lemon_sponge_discount_selling_price = (
    lemon_sponge_selling_price - lemon_sponge_seven_percent_discount_price
)
chocolate_discount_selling_price = (
    chocolate_selling_price - chocolate_seven_percent_discount_price
)

print(
    f"Get selling price after discount: {black_forest_discount_selling_price} {vanilla_discount_selling_price} {red_velvet_discount_selling_price} {lemon_sponge_discount_selling_price} {chocolate_discount_selling_price}"
)


# Owner wants to estimate total amount of profit after sell for each cake
black_forest_total_profit_after_sale = (
    black_forest_selling_price - black_forest_inventory_total_costs
)
vanilla_total_profit_after_sale = vanilla_selling_price - vanilla_inventory_total_costs
red_velvet_total_profit_after_sale = (
    red_velvet_selling_price - red_velvet_inventory_total_costs
)
lemon_sponge_total_profit_after_sale = (
    lemon_sponge_selling_price - lemon_sponge_inventory_total_costs
)
chocolate_total_profit_after_sale = (
    chocolate_selling_price - chocolate_inventory_total_costs
)

print(
    f"Total profit after sales: {black_forest_total_profit_after_sale} {vanilla_total_profit_after_sale} {red_velvet_total_profit_after_sale} {lemon_sponge_total_profit_after_sale} {chocolate_total_profit_after_sale}"
)

# Owner wants to estimate % of profit/loss after sale for each cake
black_forest_total_profit_discount_after_sales = (
    black_forest_discount_selling_price - black_forest_inventory_total_costs
)
vanilla_total_profit_discount_after_sales = (
    vanilla_discount_selling_price - vanilla_inventory_total_costs
)
red_velvet_total_profit_discount_after_sales = (
    red_velvet_discount_selling_price - red_velvet_inventory_total_costs
)
lemon_sponge_total_profit_discount_after_sales = (
    lemon_sponge_discount_selling_price - lemon_sponge_inventory_total_costs
)
chocolate_total_profit_discount_after_sales = (
    chocolate_discount_selling_price - chocolate_inventory_total_costs
)

print(
    f"Total profit after discount sales: {black_forest_total_profit_discount_after_sales} {vanilla_total_profit_discount_after_sales} {red_velvet_total_profit_discount_after_sales} {lemon_sponge_total_profit_discount_after_sales} {chocolate_total_profit_discount_after_sales}"
)
