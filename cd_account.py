# Import the Account class from the Account.py file.
from Account import Account


class CD(Account):
    """Creating a CdAccount class that inherits from the Account class."""

    def __init__(self, balance, interest):
        """Initialize the Account class."""


# Define a function for the CD Account
def create_cd_account(balance, interest_rate, maturity):
    """Creates a CD account, calculates interest earned, and updates the account balance.
    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months to determine the amount of interest.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """

    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    cd_account = Account(balance, 0)

    # Calculate interest earned
    time_years = maturity / 12
    interest_earned = balance * (interest_rate * time_years)

    # Update the CD account balance by adding the interest earned
    updated_balance = balance + interest_earned

    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    cd_account.set_balance(updated_balance)

    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    cd_account.set_interest(interest_earned)

    # Return the updated balance and interest earned.
    return updated_balance, interest_earned
