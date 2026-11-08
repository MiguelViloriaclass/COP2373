# Name: Miguel Viloria Abreu
# Date: November 7, 2026

class BankAcct:
    """
    Brief Description:
        Class to represent a bank account.
    Parameters:
        name (str): Name of the account holder.
        account_number (str): Unique identifier for the bank account.
        amount (float): Current balance in the account.
        interest_rate (float): Annual interest rate percentage.
    Variables:
        self.name (str): Account holder's name.
        self.account_number (str): Account identification number.
        self.amount (float): Current balance.
        self.interest_rate (float): Current annual interest rate.
    Logical Steps:
        1. Store account holder name, number, initial amount, and interest rate.
    Return:
        None
    """

    def __init__(self, name, account_number, amount, interest_rate):
        """
        Brief Description:
            Initializes a new BankAcct object with holder details and balance.
        Parameters:
            name (str): Name of the account holder.
            account_number (str): Unique account number.
            amount (float): Initial balance amount.
            interest_rate (float): Initial annual interest rate percentage.
        Variables:
            self.name (str): Stores the owner's name.
            self.account_number (str): Stores the account number.
            self.amount (float): Stores the current balance.
            self.interest_rate (float): Stores the interest rate percentage.
        Logical Steps:
            1. Assign parameters to object attributes.
        Return:
            None
        """
        # Save the account holder's name
        self.name = name

        # Save the account number
        self.account_number = account_number

        # Convert the initial amount to float and save it
        self.amount = float(amount)

        # Convert the interest rate to float and save it
        self.interest_rate = float(interest_rate)

    def set_interest_rate(self, new_rate):
        """
        Brief Description:
            Adjusts the annual interest rate of the account.
        Parameters:
            new_rate (float): The new annual interest rate percentage.
        Variables:
            self.interest_rate (float): Updated annual interest rate percentage.
        Logical Steps:
            1. Update self.interest_rate with the new rate.
        Return:
            None
        """
        # Update the interest rate with the new value
        self.interest_rate = float(new_rate)

    def deposit(self, amount):
        """
        Brief Description:
            Deposits a specified positive amount into the account.
        Parameters:
            amount (float): Amount of money to add to the account.
        Variables:
            self.amount (float): Updated balance after deposit.
        Logical Steps:
            1. Check if amount is greater than zero.
            2. Add amount to self.amount and print confirmation.
        Return:
            float: Updated account balance.
        """
        # If the amount is greater than zero, add it to the current balance
        if amount > 0:
            self.amount += amount
            print(f"Deposited: ${amount:,.2f}")
        else:
            print("Deposit amount must be positive.")

        return self.amount

    def withdraw(self, amount):
        """
        Brief Description:
            Withdraws a specified amount from the account if sufficient funds exist.
        Parameters:
            amount (float): Amount of money to deduct from the account.
        Variables:
            self.amount (float): Updated balance after withdrawal.
        Logical Steps:
            1. Check if amount is valid and less than or equal to balance.
            2. Subtract amount from self.amount or print error.
        Return:
            float: Updated account balance.
        """
        # Verify that we have enough money before withdrawing
        if 0 < amount <= self.amount:
            self.amount -= amount
            print(f"Withdrew: ${amount:,.2f}")
        elif amount > self.amount:
            print("Insufficient funds for this withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

        return self.amount

    def get_balance(self):
        """
        Brief Description:
            Retrieves the current account balance.
        Parameters:
            None
        Variables:
            self.amount (float): Current balance.
        Logical Steps:
            1. Return self.amount.
        Return:
            float: Current balance of the account.
        """
        # Return the current account balance
        return self.amount

    def calculate_interest(self, days):
        """
        Brief Description:
            Calculates interest accrued over a specified number of days.
        Parameters:
            days (int): Number of days to calculate interest for.
        Variables:
            daily_rate (float): Daily interest rate derived from annual percentage.
            interest_earned (float): Calculated interest earned.
        Logical Steps:
            1. Calculate daily rate from annual rate and days in year (365).
            2. Multiply balance by daily rate and number of days.
        Return:
            float: Interest amount earned over the given days.
        """
        # Convert annual rate to daily rate by dividing by 365
        daily_rate = (self.interest_rate / 100) / 365

        # Calculate interest generated based on the specified days
        interest_earned = self.amount * daily_rate * days

        return interest_earned

    def __str__(self):
        """
        Brief Description:
            Returns a string representation of the account details.
        Parameters:
            None
        Variables:
            None
        Logical Steps:
            1. Format account info into a clear string.
        Return:
            str: String containing account details.
        """
        # Build the text with the main account information
        return (
            f"Account Holder: {self.name}\n"
            f"Account Number: {self.account_number}\n"
            f"Balance: ${self.amount:,.2f}\n"
            f"Interest Rate: {self.interest_rate:.2f}%"
        )


def run_bank_account_tests():
    """
    Brief Description:
        Tests all methods of the BankAcct class to verify proper functionality.
    Parameters:
        None
    Variables:
        my_account (BankAcct): Test instance of BankAcct.
        days_to_test (int): Days to calculate interest.
        interest_amount (float): Total interest earned.
    Logical Steps:
        1. Create a BankAcct object.
        2. Test deposit, withdraw, rate change, and interest calculation methods.
    Return:
        None
    """
    # Create a test account
    print("--- Creating Bank Account ---")
    my_account = BankAcct("Miguel Viloria", "ACC-987654", 1000.00, 4.5)

    # Display the initial state using __str__
    print(my_account)
    print()

    # Test making a deposit
    print("--- Testing Deposit ---")
    my_account.deposit(500.00)
    print(f"Current Balance: ${my_account.get_balance():,.2f}\n")

    # Test making a withdrawal
    print("--- Testing Withdrawal ---")
    my_account.withdraw(200.00)
    print(f"Current Balance: ${my_account.get_balance():,.2f}\n")

    # Test changing the interest rate
    print("--- Testing Rate Update ---")
    my_account.set_interest_rate(5.25)
    print(f"New Interest Rate: {my_account.interest_rate:.2f}%\n")

    # Test calculating interest for 30 days
    print("--- Testing Interest Calculation ---")
    days_to_test = 30
    interest_amount = my_account.calculate_interest(days_to_test)
    print(f"Interest earned over {days_to_test} days: ${interest_amount:,.2f}\n")

    # Display the final account state
    print("--- Final Account Summary ---")
    print(my_account)
    print(f"Calculated Interest (30 Days): ${interest_amount:,.2f}")


def main():
    """
    Brief Description:
        Main entry point for executing the testing function.
    Parameters:
        None
    Variables:
        None
    Logical Steps:
        1. Call run_bank_account_tests.
    Return:
        None
    """
    # Execute the main tests
    run_bank_account_tests()


if __name__ == "__main__":
    # Call main when the script is run directly
    main()