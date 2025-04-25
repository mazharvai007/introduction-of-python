# Encapsulation


class BankAccount:
    def __init__(self, account_number, balance) -> None:
        """
        __account_number and __balance are private attributes. We will not be able to access them from outside of the class
        """

        self.__account_number = account_number
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


# Usage
account = BankAccount("123456789", 150050)
account.deposit(150000)
account.withdraw(2000)
print(account.get_balance())
