class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self,initial_amount,acc_name):
        self.balance=initial_amount
        self.name=acc_name

        print(f"\nAccount '{self.name}' created.\n Balance=${self.balance:.2f}")

    def getbalance(self):
        print(f"\nAccount '{self.name}' has Balance=${self.balance:.2f}")

    def deposit(self,amount):
        self.balance += amount
        print("\nDeposit complete.")
        self.getbalance()

    def viableTransaction(self,amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry,Acount '{self.name}' has only a balance of ${self.balance:.2f}"
            )

    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print("\nWithdraw complete.")
            self.getbalance()
        except BalanceException as error:
            print(f"\nWithdraw Interrupted! {error}")

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
        
