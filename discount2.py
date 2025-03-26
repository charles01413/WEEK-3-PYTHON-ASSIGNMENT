def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        # Calculate the final price after applying the discount
        return price - (price * discount_percent / 100)
    else:
        # Return the original price if discount is less than 20%
        return price

# User input and output
try:
    # Prompt the user to put inputs
    price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Use function to calculate the final price
    final_price = calculate_discount(price, discount_percent)

    # Give the result
    if final_price < price:
        print(f"The final price after applying the discount is: {final_price:.2f}")
    else:
        print(f"No discount applied. The original price remains: {price:.2f}")
except ValueError:
    # Handle invalid user input
    print("Invalid input. Please enter numeric values for price and discount.")
