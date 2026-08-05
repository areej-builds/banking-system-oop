# Custom exception used when an account doesn't have enough balance
# for a withdrawal or transfer.
class BalanceException(Exception):
    pass


class BankAccount:
    # Creates a new account with a starting balance and owner name.
    def __init__(self,initial_amount,acc_name):
        self.balance=initial_amount
        self.name=acc_name

        print(f"\nAccount '{self.name}' created.\n Balance=${self.balance:.2f}")

    # Prints the current balance of the account.
    def getbalance(self):
        print(f"\nAccount '{self.name}' has Balance=${self.balance:.2f}")

    # Adds the given amount to the balance.
    def deposit(self,amount):
        self.balance += amount
        print("\nDeposit complete.")
        self.getbalance()

    # Checks whether the account has enough balance for the given amount.
    # Raises BalanceException if not.
    def viableTransaction(self,amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry,Acount '{self.name}' has only a balance of ${self.balance:.2f}"
            )

    # Withdraws the given amount if the balance allows it,
    # otherwise catches the exception and prints a friendly message.
    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print("\nWithdraw complete.")
            self.getbalance()
        except BalanceException as error:
            print(f"\nWithdraw Interrupted! {error}")

    # Transfers the given amount from this account to another BankAccount object.
    # Withdraws from self first, then deposits into the target account.
    def transfer(self,account,amount):
        try:
            print("\n"+ "="*30)
            print("\nBegining the tranfer...")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer Complete!")
            print("\n", "="*30)

        except BalanceException as error:
            print(f"\nSorry, Transfer Interrupted! {error}")
            print("\n"+ "="*30)


# A BankAccount that rewards every deposit with a 5% bonus.
class InterestRewardAcc(BankAccount):
    # Overrides deposit() to add 5% extra on top of the deposited amount.
    def deposit(self, amount):
        self.balance += (amount*1.05)
        print("Deposit complete.")
        self.getbalance()


# An InterestRewardAcc that also charges a flat fee on every withdrawal.
class SavingAcc(InterestRewardAcc):
    # Same as BankAccount's init, but also sets a fixed withdrawal fee.
    def __init__(self, initial_amount, acc_name):
        super().__init__(initial_amount, acc_name)
        self.fee=5.0

    # Overrides withdraw() to deduct the withdrawal amount plus the fee.
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount+self.fee)
            self.balance -= (amount + self.fee)
            print("\nWithdraw complete.")
            self.getbalance()

        except BalanceException as error:
            print(f"\nWithdraw Interrupted! {error}")