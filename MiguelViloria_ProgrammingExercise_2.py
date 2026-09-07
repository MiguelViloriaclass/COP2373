# Author: Miguel Viloria
# Date: September 06, 2026

def calculate_discount(price, discount_rate):
    """
    Calculates the discount amount based on the price and discount rate.

    Parameters:
        price (int or float): The original price of the product.
        discount_rate (float): The discount rate as a decimal.

    Variables:
        discount_amount (float): The calculated amount of discount.

    Logic:
        1. Multiply the price by the discount rate.
        2. Return the calculated discount amount.

    Return:
        float: The amount to be discounted from the original price.
    """
    # Calculate the discount amount by multiplying price and rate
    discount_amount = price * discount_rate
    return discount_amount


def apply_discount(price, discount_amount):
    """
    Applies the discount amount to the original price to get the final price.

    Parameters:
        price (int or float): The original price of the product.
        discount_amount (float): The discount amount to subtract.

    Variables:
        new_price (float): The final price after applying the discount.

    Logic:
        1. Subtract the discount amount from the original price.
        2. Return the new final price.

    Return:
        float: The final price after discount.
    """
    # Subtract discount amount from original price
    new_price = price - discount_amount
    return new_price


def main():
    """
    Main function to iterate through products, process prices, and handle errors.

    Parameters:
        None

    Variables:
        products (list): A list of dictionaries representing products.
        product (dict): Individual product item from the products list.
        price (int or float): Processed numeric price of a product.
        discount_rate (float): Processed numeric discount rate.
        discount_amount (float): Calculated discount for the product.
        final_price (float): Final price after discount.

    Logic:
        1. Define a list of product dictionaries.
        2. Loop through each product in the list.
        3. Convert price and discount rate to float using try-except block.
        4. Calculate discount and final price if conversion succeeds.
        5. Display product details or an error message if invalid data exists.

    Return:
        None
    """
    # Define product inventory list with potential data type errors
    products = [
        {"name": "Laptop", "price": 1000, "discount_rate": 0.1},
        {"name": "Smartphone", "price": 800, "discount_rate": 0.15},
        {"name": "Tablet", "price": "500", "discount_rate": 0.2},
        {"name": "Headphones", "price": 200, "discount_rate": 0.05}
    ]

    # Iterate through each product in the inventory
    for product in products:
        try:
            # Convert values to float to handle potential string inputs
            price = float(product["price"])
            discount_rate = float(product["discount_rate"])

            # Calculate discount amount and final price
            discount_amount = calculate_discount(price, discount_rate)
            final_price = apply_discount(price, discount_amount)

            # Output the processed product details
            print(f"Product: {product['name']}")
            print(f"Original Price: ${price:.2f}")
            print(f"Discount Amount: ${discount_amount:.2f}")
            print(f"Final Price: ${final_price:.2f}\n")

        except (ValueError, TypeError) as error_msg:
            # Handle invalid numeric input gracefully
            print(f"Error processing {product.get('name', 'Unknown')}: {error_msg}\n")


if __name__ == "__main__":
    # Call the main execution function
    main()