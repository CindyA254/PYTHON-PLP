def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# user to enter the original price and discount percentage
original_price = float(input("Enter the original price of the item: $"))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculating the final price after applying the discount
final_price = calculate_discount(original_price, discount_percentage)

# Printing the final price
print(f"The final price after applying the discount is: ${final_price:.2f}")
