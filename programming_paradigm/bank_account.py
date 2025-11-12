class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the account with an optional starting balance (default is 0)."""
        self.__account_balance = initial_balance  # Encapsulated attribute

    def deposit(self, amount):
        """Add the specified amount to the account balance."""
        if amount > 0:
            self.__account_balance += amount
        else:
            raise ValueError("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Deduct the amount if sufficient funds exist; otherwise return False."""
        if amount > self.__account_balance:
            return False
        self.__account_balance -= amount
        return True

    def display_balance(self):
        """Display the current account balance in a user-friendly format."""
        print(f"Current Balance: ${self.__account_balance}")
