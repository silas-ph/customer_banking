# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account


# Define the main function
def main():

    # This function prompts the user to enter the savings and cd account balance, interest rate,
    # and the length of months to determine the interest gained.
    # It displays the interest earned on the savings and CD accounts and updates the balances.
    # Savings account user inputs
    savings_balance = float(input("What is your savings account balance? "))
    savings_interest = (
        float(input("What is the APR for the savings account (e.g., 2.5 for 2.5%): "))
        / 100
    )
    savings_months = int(input("How many months will the money be in the account? "))
    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, interest_earned = create_savings_account(
        savings_balance, savings_interest, savings_months
    )
    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(
        f"The interest earned (simple interest) on the savings account is: ${interest_earned:,.2f}, and your updated balance is: ${updated_savings_balance:,.2f}.\n"
    )

    # CD account user inputs
    cd_balance = float(input("What is your CD account balance? "))
    cd_interest = (
        float(input("What is the APR for the CD account (e.g., 2.5 for 2.5%): ")) / 100
    )
    cd_maturity = int(input("What is the maturity of your CD, in months? "))

    print(f"CD Balance: {cd_balance:,.2f}")
    print(f"CD Interest Rate (APR): {cd_interest * 100}%")
    print(f"CD Maturity Period (Months): {cd_maturity}")

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, interest_earned = create_cd_account(
        cd_balance, cd_interest, cd_maturity
    )

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print(
        f"The interest earned on your CD account is: ${interest_earned:,.2f}, and your updated balance is: ${updated_cd_balance:,.2f}.\n"
    )


if __name__ == "__main__":
    main()  # Call the main function.
