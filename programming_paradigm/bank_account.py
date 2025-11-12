class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an optional starting balance (default 0)."""
        self.__account_balance = initial_balance  # private attribute

    def deposit(self, amount):
        """Add amount to balance."""
        if amount > 0:
            self.__account_balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Subtract amount from balance if sufficient funds exist; otherwise return False."""
        if amount > self.__account_balance:
            return False
        self.__account_balance -= amount
        return True

    def display_balance(self):
        """Print current balance formatted to 2 decimal places."""
        print(f"Current Balance: ${self.__account_balance:.2f}")
