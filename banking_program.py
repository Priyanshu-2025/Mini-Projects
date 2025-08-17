"""
Banking Program in Python
-------------------------
This is a simple Banking System that allows:
- Creating an account
- Viewing balance
- Depositing money
- Withdrawing money
"""

class BankAccount:
    """Class representing a simple bank account."""

    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"✅ Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("❌ Deposit amount must be positive.")

    def withdraw(self, amount: float):
        """Withdraw money from the account."""
        if amount > self.balance:
            print("❌ Insufficient funds.")
        elif amount <= 0:
            print("❌ Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"✅ Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def view_balance(self):
        """Display current account balance."""
        print(f"💰 {self.owner}, your current balance is: ${self.balance:.2f}")


def main():
    """Main menu for the banking program."""
    print("🏦 Welcome to SimpleBank!")
    name = input("Enter your name to create an account: ")
    account = BankAccount(owner=name)

    while True:
        print("\n--- Banking Menu ---")
        print("1. View Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Select an option (1-4): ")

        if choice == "1":
            account.view_balance()
        elif choice == "2":
            try:
                amount = float(input("Enter amount to deposit: "))
                account.deposit(amount)
            except ValueError:
                print("❌ Please enter a valid number.")
        elif choice == "3":
            try:
                amount = float(input("Enter amount to withdraw: "))
                account.withdraw(amount)
            except ValueError:
                print("❌ Please enter a valid number.")
        elif choice == "4":
            print("👋 Thank you for using SimpleBank. Goodbye!")
            break
        else:
            print("❌ Invalid option. Please choose again.")


if __name__ == "__main__":
    main()
