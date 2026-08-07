from bank_accounts import *

# Load any previously saved accounts when the program starts
accounts = load_accounts()


def find_account(name):
    return accounts.get(name)


def verify_pin(acc):
    entered = input(f"Enter PIN for '{acc.name}': ").strip()
    if not acc.check_pin(entered):
        print("\nIncorrect PIN. Action cancelled.")
        return False
    return True


def get_amount(prompt):
    '''Asks for a number and returns it, or None if the input isn't valid.'''
    raw = input(prompt).strip()
    try:
        return float(raw)
    except ValueError:
        print("\nInvalid amount: please enter a number.")
        return None


def create_account():
    name = input("Enter account holder name: ").strip()
    if not name:
        print("\nAccount name cannot be empty.")
        return
    if name in accounts:
        print(f"\nAn account named '{name}' already exists.")
        return

    amount = get_amount("Enter initial balance: ")
    if amount is None or amount < 0:
        print("\nInvalid starting balance.")
        return

    pin = input("Set a 4-digit PIN: ").strip()

    print("\nChoose account type:")
    print("1. Regular BankAccount")
    print("2. InterestRewardAcc (5% deposit bonus)")
    print("3. SavingAcc (5% deposit bonus + withdrawal fee)")
    choice = input("Enter choice (1-3): ").strip()

    if choice == "2":
        acc = InterestRewardAcc(amount, name, pin)
    elif choice == "3":
        acc = SavingAcc(amount, name, pin)
    else:
        acc = BankAccount(amount, name, pin)

    accounts[name] = acc
    save_accounts(accounts)


def deposit_flow():
    acc = find_account(input("Account name: ").strip())
    if not acc:
        print("\nAccount not found.")
        return
    if not verify_pin(acc):
        return

    amount = get_amount("Deposit amount: ")
    if amount is None:
        return

    acc.deposit(amount)
    save_accounts(accounts)


def withdraw_flow():
    acc = find_account(input("Account name: ").strip())
    if not acc:
        print("\nAccount not found.")
        return
    if not verify_pin(acc):
        return

    amount = get_amount("Withdraw amount: ")
    if amount is None:
        return

    acc.withdraw(amount)
    save_accounts(accounts)


def transfer_flow():
    from_acc = find_account(input("From account: ").strip())
    if not from_acc:
        print("\nAccount not found.")
        return
    if not verify_pin(from_acc):
        return

    to_acc = find_account(input("To account: ").strip())
    if not to_acc:
        print("\nTarget account not found.")
        return

    amount = get_amount("Transfer amount: ")
    if amount is None:
        return

    from_acc.transfer(to_acc, amount)
    save_accounts(accounts)


def check_balance_flow():
    acc = find_account(input("Account name: ").strip())
    if not acc:
        print("\nAccount not found.")
        return
    acc.getbalance()


def statement_flow():
    name = input("Account name: ").strip()
    if name not in accounts:
        print("\nAccount not found.")
        return
    account_statement(name)


def compare_flow():
    compare_accounts(accounts)


def show_menu():
    print("\n" + "=" * 30)
    print("      BANKING SYSTEM MENU")
    print("=" * 30)
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transfer")
    print("5. Check Balance")
    print("6. Account Statement")
    print("7. Compare Accounts")
    print("8. Exit")


def main_menu():
    while True:
        show_menu()
        choice = input("Choose an option (1-8): ").strip()

        if choice == "1":
            create_account()
        elif choice == "2":
            deposit_flow()
        elif choice == "3":
            withdraw_flow()
        elif choice == "4":
            transfer_flow()
        elif choice == "5":
            check_balance_flow()
        elif choice == "6":
            statement_flow()
        elif choice == "7":
            compare_flow()
        elif choice == "8":
            save_accounts(accounts)
            print("\nAll accounts saved. Goodbye!")
            break
        else:
            print("\nInvalid choice, please try again.")


if __name__ == "__main__":
    main_menu()