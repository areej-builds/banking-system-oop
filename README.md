# Banking System OOP

Simple bank account management system in Python using OOP principles.

## Overview

This project demonstrates core Object-Oriented Programming concepts in Python — encapsulation, inheritance, and custom exception handling — through a simulated banking system. It supports creating accounts, depositing, withdrawing, and transferring funds between accounts, with built-in checks to prevent invalid transactions (e.g., withdrawing more than the available balance). It also includes specialized account types that reward deposits with bonus interest, and a full interactive CLI menu with PIN-protected transactions and persistent storage.

## Features

- Interactive CLI menu — create accounts, deposit, withdraw, transfer, check balance, view statements, and compare accounts
- Create bank accounts with an initial balance, account holder name, and a 4-digit PIN
- PIN protection — deposits, withdrawals, and transfers require PIN verification before proceeding
- Check account balance
- Deposit funds
- Withdraw funds (with balance validation)
- Transfer funds between two accounts
- Custom `BalanceException` for handling insufficient-funds errors gracefully
- `InterestRewardAcc` — a special account type that adds a 5% bonus on every deposit
- `SavingAcc` — inherits from `InterestRewardAcc`, also charges a flat $5 fee on every withdrawal
- Transaction logging — every deposit, withdraw, and transfer is automatically recorded in `history.json`
- Account persistence — all accounts (type, balance, PIN) are saved to `accounts.json` and automatically reloaded the next time the program runs
- Account statements — view a full transaction history and totals for any account
- Account comparison — list all accounts sorted from highest to lowest balance

## Project Structure

```
banking-system-oop/
├── bank_accounts.py    # BankAccount, BalanceException, InterestRewardAcc, SavingAcc classes + persistence & reporting helpers
├── main.py             # Entry point — interactive CLI menu wired to all account operations
├── accounts.json        # Auto-generated account storage (ignored by git)
├── history.json         # Auto-generated transaction log (ignored by git)
├── output_files/       # Screenshots of sample program output
└── README.md
```
> Note: `accounts.json` and `history.json` are listed in `.gitignore` since they're generated at runtime and differ per user/run — they aren't tracked in the repo.

## Requirements

- Python 3.x (no external libraries needed)

## How to Run

1. Clone the repository:

```
git clone https://github.com/areej-builds/banking-system-oop.git
cd banking-system-oop
```

2. Run the main script:

```
python main.py
```

3. Use the on-screen menu to create accounts and perform transactions. Your accounts and transaction history are saved automatically and will still be there the next time you run the program.

## Menu Options

```
==============================
      BANKING SYSTEM MENU
==============================
1. Create Account
2. Deposit
3. Withdraw
4. Transfer
5. Check Balance
6. Account Statement
7. Compare Accounts
8. Exit
```

- **Create Account** — choose a name, starting balance, PIN, and account type (Regular, InterestRewardAcc, or SavingAcc)
- **Deposit / Withdraw / Transfer** — require the account's PIN before the transaction is processed
- **Check Balance** — prints the current balance for an account
- **Account Statement** — prints every transaction for an account along with total deposited/withdrawn
- **Compare Accounts** — lists all accounts sorted by balance, highest to lowest
- **Exit** — saves all accounts to `accounts.json` before quitting

## Classes

### `BankAccount`

Base class representing a standard bank account.

- `check_pin(entered_pin)` — verifies the entered PIN matches the account's PIN
- `getbalance()` — prints the current balance
- `deposit(amount)` — adds funds to the balance
- `withdraw(amount)` — removes funds, blocked if balance is insufficient
- `transfer(account, amount)` — withdraws from self and deposits into another `BankAccount` object
- `SavingDataToFile(action, amount)` — logs each transaction (account, action, amount, resulting balance) to `history.json`

### `InterestRewardAcc` (inherits from `BankAccount`)

A reward account that overrides `deposit()` to add a 5% bonus on every deposit — e.g., depositing $100 adds $105 to the balance.

### `SavingAcc` (inherits from `InterestRewardAcc`)

Keeps the 5% deposit bonus and additionally charges a flat $5 fee on every withdrawal — overrides `withdraw()` to deduct the withdrawal amount plus the fee.

### `BalanceException`

Custom exception raised when a withdrawal or transfer is attempted with insufficient funds. Caught internally so the program doesn't crash — it prints a friendly error message instead.

## Persistence

- `save_accounts()` — writes every account's type, balance, and PIN to `accounts.json`
- `load_accounts()` — reads `accounts.json` on startup and rebuilds each account object with the correct class (`BankAccount`, `InterestRewardAcc`, or `SavingAcc`)
- Accounts are saved automatically after every operation and again on exit, so no data is lost between runs

## Concepts Demonstrated

- **Classes & Objects** — modeling real-world entities (bank accounts) as Python objects
- **Encapsulation** — balance, PIN, and account logic bundled within the `BankAccount` class
- **Inheritance & Method Overriding** — `InterestRewardAcc` extends `BankAccount`, and `SavingAcc` extends `InterestRewardAcc`, each customizing `deposit()` / `withdraw()`
- **Custom Exceptions** — `BalanceException` for domain-specific error handling
- **Method Interaction** — `transfer()` reusing `withdraw()` and `deposit()` internally, and working polymorphically across account types
- **File Handling** — accounts and transactions are read, appended/rebuilt, and rewritten as valid JSON, giving persistent state across runs
- **CLI Design** — a menu-driven interface separating user interaction (`main.py`) from business logic (`bank_accounts.py`)

## Author

Areej