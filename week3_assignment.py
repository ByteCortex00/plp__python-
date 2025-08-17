def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount = price * (discount_percent / 100)
        final_price = price - discount
        return final_price
    else:
        return price

# Get user input
price = float(input("Enter the item price: "))
discount_percent = float(input("Enter discount percent: "))

# Calculate final price
final_price = calculate_discount(price, discount_percent)

print(f"The final price is: {final_price}")
