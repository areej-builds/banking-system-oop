import json
import os

HISTORY_FILE = "history.json"
ACCOUNTS_FILE = "accounts.json"


class BalanceException(Exception):
    '''
    Custom exception raised when an account doesn't have enough balance
    for a withdrawal or transfer. Used by viableTransaction(), withdraw(),
    and transfer() to fail gracefully instead of crashing the program.
    '''
    pass


class BankAccount:
    '''
    Base class representing a standard bank account.
    Supports creating an account, checking balance, depositing, withdrawing,
    and transferring funds to another BankAccount. Uses BalanceException
    to handle cases where a withdrawal/transfer amount exceeds the balance,
    validates amounts before touching the balance, and logs every
    transaction to history.json.
    '''

    def __init__(self, initial_amount, acc_name, pin="0000", _loading=False):
        '''Creates a new account with a starting balance, owner name, and PIN.'''
        self.balance = initial_amount
        self.name = acc_name
        self.pin = str(pin)

        if not _loading:
            print(f"\nAccount '{self.name}' created.\n Balance=${self.balance:.2f}")

    def check_pin(self, entered_pin):
        '''Returns True if the entered PIN matches this account's PIN.'''
        return str(entered_pin) == self.pin

    def getbalance(self):
        '''Prints the current balance.'''
        print(f"\nAccount '{self.name}' has Balance=${self.balance:.2f}")

    def validate_amount(self, amount):
        '''Returns True only if amount is a positive number.'''
        if not isinstance(amount, (int, float)):
            print("\nInvalid amount: must be a number.")
            return False
        if amount <= 0:
            print("\nInvalid amount: must be greater than zero.")
            return False
        return True

    def deposit(self, amount):
        '''Adds the given amount to the balance, after validating it.'''
        if not self.validate_amount(amount):
            return
        self.balance += amount
        print("\nDeposit complete.")
        self.getbalance()
        self.SavingDataToFile("Deposit", amount)

    def viableTransaction(self, amount):
        '''Raises BalanceException if the balance is too low for this amount.'''
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry,Acount '{self.name}' has only a balance of ${self.balance:.2f}"
            )

    def withdraw(self, amount):
        '''
        Withdraws the amount if it's valid and funds allow, otherwise
        catches BalanceException and fails gracefully with a message.
        '''
        if not self.validate_amount(amount):
            return
        try:
            self.viableTransaction(amount)
            self.balance -= amount
            print("\nWithdraw complete.")
            self.getbalance()
            self.SavingDataToFile("Withdraw", amount)
        except BalanceException as error:
            print(f"\nWithdraw Interrupted! {error}")

    def transfer(self, account, amount):
        '''
        Withdraws from self and deposits into another BankAccount object.
        Catches BalanceException if the transfer amount is too high.
        '''
        if not self.validate_amount(amount):
            return
        try:
            print("\n" + "=" * 30)
            print("\nBegining the tranfer...")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer Complete!")
            print("\n" + "=" * 30)
            self.SavingDataToFile(f"Transfer to {account.name}", amount)
        except BalanceException as error:
            print(f"\nSorry, Transfer Interrupted! {error}")
            print("\n" + "=" * 30)

    def SavingDataToFile(self, action, amount):
        '''
        Records a transaction entry into history.json.
        Reads any existing history first, appends the new entry, then
        rewrites the whole file so it stays valid JSON.
        '''
        entry = {
            "Account Name: ": self.name,
            "Action: ": action,
            "Amount: ": amount,
            "Current Balance: ": self.balance,
        }

        if os.path.exists(HISTORY_FILE) and os.path.getsize(HISTORY_FILE) > 0:
            with open(HISTORY_FILE, "r") as file:
                history = json.load(file)
        else:
            history = []

        history.append(entry)

        with open(HISTORY_FILE, "w") as file:
            json.dump(history, file, indent=4)


class InterestRewardAcc(BankAccount):
    '''
    A BankAccount that rewards every deposit with a 5% bonus.
    Inherits withdraw(), transfer(), and BalanceException handling
    from BankAccount unchanged; only deposit() is overridden.
    '''

    def deposit(self, amount):
        '''Overrides deposit() to add 5% extra on top of the amount.'''
        if not self.validate_amount(amount):
            return
        self.balance += (amount * 1.05)
        print("Deposit complete.")
        self.getbalance()
        self.SavingDataToFile("Deposit (with bouns)", amount)


class SavingAcc(InterestRewardAcc):
    '''
    An InterestRewardAcc that also charges a flat fee on every withdrawal.
    Keeps the 5% deposit bonus from InterestRewardAcc, but overrides
    withdraw() to deduct an extra fee and still uses BalanceException
    to block withdrawals that would exceed the balance (including the fee).
    '''

    def __init__(self, initial_amount, acc_name, pin="0000", _loading=False):
        '''Same as BankAccount's init, but also sets a fixed withdrawal fee.'''
        super().__init__(initial_amount, acc_name, pin, _loading)
        self.fee = 5.0

    def withdraw(self, amount):
        '''Overrides withdraw() to deduct the amount plus the fee.'''
        if not self.validate_amount(amount):
            return
        try:
            self.viableTransaction(amount + self.fee)
            self.balance -= (amount + self.fee)
            print("\nWithdraw complete.")
            self.getbalance()
            self.SavingDataToFile("Withdraw (with fee)", amount)

        except BalanceException as error:
            print(f"\nWithdraw Interrupted! {error}")


# ---------------------------------------------------------------------------
# Persistence helpers (save/load account state so it survives program exit)
# ---------------------------------------------------------------------------

def save_accounts(accounts):
    '''Saves every account's type, balance, and PIN to accounts.json.'''
    data = {}
    for name, acc in accounts.items():
        entry = {
            "type": type(acc).__name__,
            "balance": acc.balance,
            "pin": acc.pin,
        }
        data[name] = entry

    with open(ACCOUNTS_FILE, "w") as file:
        json.dump(data, file, indent=4)


def load_accounts():
    '''Loads accounts.json (if it exists) and rebuilds the account objects.'''
    accounts = {}

    if not (os.path.exists(ACCOUNTS_FILE) and os.path.getsize(ACCOUNTS_FILE) > 0):
        return accounts

    with open(ACCOUNTS_FILE, "r") as file:
        data = json.load(file)

    for name, info in data.items():
        acc_type = info.get("type", "BankAccount")
        balance = info.get("balance", 0)
        pin = info.get("pin", "0000")

        if acc_type == "InterestRewardAcc":
            acc = InterestRewardAcc(balance, name, pin, _loading=True)
        elif acc_type == "SavingAcc":
            acc = SavingAcc(balance, name, pin, _loading=True)
        else:
            acc = BankAccount(balance, name, pin, _loading=True)

        accounts[name] = acc

    return accounts


# -----------------------------------------------------------
# Reporting helpers
# -----------------------------------------------------------

def account_statement(name):
    '''Prints every transaction for the given account name, with totals.'''
    if not (os.path.exists(HISTORY_FILE) and os.path.getsize(HISTORY_FILE) > 0):
        print("\nNo transaction history found.")
        return

    with open(HISTORY_FILE, "r") as file:
        history = json.load(file)

    entries = [e for e in history if e.get("Account Name: ") == name]

    if not entries:
        print(f"\nNo transactions found for '{name}'.")
        return

    print(f"\n--- Statement for {name} ---")
    total_deposit = 0
    total_withdraw = 0

    for e in entries:
        action = e.get("Action: ", "")
        amount = e.get("Amount: ", 0)
        balance = e.get("Current Balance: ", 0)
        print(f"{action}: ${amount:.2f}  ->  Balance: ${balance:.2f}")

        if "Deposit" in action:
            total_deposit += amount
        elif "Withdraw" in action:
            total_withdraw += amount

    print(f"\nTotal Deposited: ${total_deposit:.2f}")
    print(f"Total Withdrawn: ${total_withdraw:.2f}")


def compare_accounts(accounts):
    '''Prints all accounts sorted from highest to lowest balance.'''
    if not accounts:
        print("\nNo accounts to compare.")
        return

    sorted_accounts = sorted(accounts.values(), key=lambda a: a.balance, reverse=True)

    print("\n--- Account Comparison (highest to lowest balance) ---")
    for acc in sorted_accounts:
        print(f"{acc.name} ({type(acc).__name__}): ${acc.balance:.2f}")