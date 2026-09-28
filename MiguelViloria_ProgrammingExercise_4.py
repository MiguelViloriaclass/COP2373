"""
Name: Miguel Viloria
Date: September 27, 2026
Description: Program that collects monthly expenses, calculates total, highest,
and lowest expense using reduce, and prints the summary.
"""

from functools import reduce


def get_expenses():
    """
    Prompts the user to enter expense types and amounts until finished.

    Parameters:
        None

    Variables:
        expenses (list): List of dictionaries with expense type and amount.
        expense_type (str): Type or name of expense.
        amount (float): Amount of the expense.

    Logical Steps:
        1. Initialize empty expenses list.
        2. Prompt user for expense name and valid numeric amount.
        3. Append dictionary to expenses list.
        4. Ask if user wants to continue.
        5. Return list of expenses.

    Returns:
        list: List of expense dictionaries.
    """
    expenses = []

    while True:
        # Get expense type and cost
        expense_type = input("Enter expense type: ").strip()
        while True:
            try:
                amount = float(input(f"Enter amount for {expense_type}: $"))
                if amount >= 0:
                    break
                print("Amount must be positive.")
            except ValueError:
                print("Enter a valid number.")

        expenses.append({"type": expense_type, "amount": amount})

        # Ask to keep adding
        if input("Add another? (y/n): ").strip().lower() not in ("yes", "y"):
            break

    return expenses


def analyze_and_display(expenses):
    """
    Calculates total, highest, and lowest expense using reduce and prints results.

    Parameters:
        expenses (list): List of expense dictionaries.

    Variables:
        total (float): Total sum of expenses.
        highest (dict): Expense dict with maximum amount.
        lowest (dict): Expense dict with minimum amount.

    Logical Steps:
        1. Check if expenses list is empty.
        2. Use reduce to sum amounts.
        3. Use reduce to find max expense dict.
        4. Use reduce to find min expense dict.
        5. Print total, highest, and lowest expenses.

    Returns:
        None
    """
    if not expenses:
        print("No expenses recorded.")
        return

    # Calculate total, highest, and lowest using reduce
    total = reduce(lambda acc, exp: acc + exp["amount"], expenses, 0.0)
    highest = reduce(lambda a, b: a if a["amount"] > b["amount"] else b, expenses)
    lowest = reduce(lambda a, b: a if a["amount"] < b["amount"] else b, expenses)

    # Print summary
    print("\n--- Expense Analysis Summary ---")
    print(f"Total Expenses: ${total:,.2f}")
    print(f"Highest Expense: {highest['type']} (${highest['amount']:,.2f})")
    print(f"Lowest Expense: {lowest['type']} (${lowest['amount']:,.2f})")


def main():
    """
    Main program function.

    Parameters:
        None

    Variables:
        expenses (list): List of expenses from user.

    Logical Steps:
        1. Call get_expenses to collect data.
        2. Call analyze_and_display to process and show results.

    Returns:
        None
    """
    print("Welcome to the Monthly Expense Analyzer\n")
    expenses = get_expenses()
    analyze_and_display(expenses)


if __name__ == "__main__":
    main()