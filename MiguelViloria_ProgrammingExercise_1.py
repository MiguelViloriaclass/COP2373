# Programming Exercise 1: Cinema Ticket Pre-Sale
# Author: Miguel Viloria
# Date: August 29, 2026

def get_tickets(remaining_tickets):
    """
    Brief description:
    Prompts the user to enter the number of tickets they want to buy and
    validates that the input is between 1 and 4, and does not exceed remaining.

    Parameters:
    remaining_tickets (int): The current number of available tickets.

    Variables used:
    desired_tickets (int): The number of tickets requested by the user.

    Logical steps:
    1. Start a loop to repeatedly ask for input until a valid quantity is entered.
    2. Read input from the user and convert to integer.
    3. Check if desired_tickets is less than 1 or greater than 4.
    4. Check if desired_tickets is greater than remaining_tickets.
    5. Print error messages if validation fails.
    6. Return valid desired_tickets.

    Return:
    int: The validated number of tickets the user wants to buy.
    """
    # Keep asking until user provides a valid ticket count
    while True:
        # Get input from user
        desired_tickets = int(input("How many tickets would you like to buy ? "))

        # Check if requested tickets are within valid limits
        if desired_tickets < 1 or desired_tickets > 4:
            print("Sorry, you can only buy between 1 and 4 tickets per order.")
        elif desired_tickets > remaining_tickets:
            print("Sorry, there are only " + str(remaining_tickets) + " tickets left.")
        else:
            # Valid choice, return value to caller
            return desired_tickets


def main():
    """
    Brief description:
    Main function that manages the ticket pre-sale process and tracks buyers.

    Parameters:
    None

    Variables used:
    TOTAL_TICKETS (int): Constant for maximum total tickets available (20).
    remaining_tickets (int): Number of tickets left to sell.
    total_buyers (int): Accumulator variable to count number of buyers.
    tickets_bought (int): Quantity of tickets bought in the current transaction.

    Logical steps:
    1. Initialize total tickets to 20 and buyer accumulator to 0.
    2. Print welcome message.
    3. Loop until remaining_tickets reaches 0.
    4. Call get_tickets() to get valid number of tickets from user.
    5. Subtract tickets bought from remaining_tickets.
    6. Increment buyer accumulator by 1.
    7. Display remaining tickets left.
    8. Display completion message and total number of buyers when finished.

    Return:
    None
    """
    # Define constant for initial ticket amount
    TOTAL_TICKETS = 20

    # Initialize variables
    remaining_tickets = TOTAL_TICKETS
    total_buyers = 0

    print("--- Welcome to the Cinema Ticket Pre-Sale Hollywood ---")
    print("Total tickets available: " + str(TOTAL_TICKETS))
    print()

    # Loop until all tickets are sold out
    while remaining_tickets > 0:
        # Get valid number of tickets from user
        tickets_bought = get_tickets(remaining_tickets)

        # Update remaining tickets and buyer accumulator
        remaining_tickets = remaining_tickets - tickets_bought
        total_buyers = total_buyers + 1

        # Display current status
        print("Purchase successful!")
        print("Tickets remaining: " + str(remaining_tickets))
        print()

    # Final output after loop finishes
    print("All tickets have been sold out!")
    print("Total number of buyers: " + str(total_buyers))


# Execute main function
if __name__ == "__main__":
    main()