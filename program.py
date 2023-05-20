# Catalog with product details
catalog = {
    "Product A": 20,
    "Product B": 40,
    "Product C": 50
}

# Discount rules
flat_10_discount = (200, 10)  
bulk_5_discount = (10, 5)   
bulk_10_discount = (20, 10)  
tiered_50_discount = (30, 50) 

# Fees
gift_wrap_fee = 1
shipping_fee = 5

# Prompt user for product quantities and gift wrapping choices
quantities = []
gift_wrapping = []

for product in catalog:
    quantities.append(int(input(f"Enter the quantity of {product}: ")))
    gift_wrapping.append(input(f"Wrap {product} as a gift? (yes/no): ").lower() == "yes")

# Calculate total amount for each product
total_amounts = [catalog[product] * quantities[i] for i, product in enumerate(catalog)]

# Calculate subtotal
subtotal = sum(total_amounts)

# Apply discount rule
discount_amount = 0

if subtotal > flat_10_discount[0]:
    discount_amount = flat_10_discount[1]
elif any(quantity > bulk_5_discount[0] for quantity in quantities):
    for i, quantity in enumerate(quantities):
        if quantity > bulk_5_discount[0]:
            discount_amount += total_amounts[i] * bulk_5_discount[1] / 100
elif sum(quantities) > bulk_10_discount[0]:
    discount_amount = subtotal * bulk_10_discount[1] / 100
elif sum(quantities) > tiered_50_discount[0] and any(quantity > 15 for quantity in quantities):
    for i, quantity in enumerate(quantities):
        if quantity > 15:
            discount_amount += total_amounts[i] * tiered_50_discount[1] / 100

# Calculate shipping fee and gift wrap fee
num_packages = sum(quantities) // 10
shipping_fee_total = num_packages * shipping_fee
gift_wrap_fee_total = sum(quantities) * gift_wrap_fee

# Calculate total amount
total = subtotal - discount_amount + shipping_fee_total + gift_wrap_fee_total

# Output the details
print("Product Details:")
for i, product in enumerate(catalog):
    print(f"{product}: Quantity: {quantities[i]}, Total Amount: ${total_amounts[i]}")

print(f"Subtotal: ${subtotal}")
print(f"Discount Applied: ${discount_amount}")
print(f"Shipping Fee: ${shipping_fee_total}")
print(f"Gift Wrap Fee: ${gift_wrap_fee_total}")
print(f"Total: ${total}")

