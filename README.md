# Banking System OOP

Simple bank account management system in Python using OOP principles.

## Overview

This project demonstrates core Object-Oriented Programming concepts in Python — encapsulation, custom exception handling, and class-based design — through a simulated banking system. It supports creating accounts, depositing, withdrawing, and transferring funds between accounts, with built-in checks to prevent invalid transactions (e.g., withdrawing more than the available balance).

## Features

- Create bank accounts with an initial balance and account holder name
- Check account balance
- Deposit funds
- Withdraw funds (with balance validation)
- Transfer funds between two accounts
- Custom `BalanceException` for handling insufficient-funds errors gracefully

## Project Structure

```
banking-system-oop/
├── bank_account.py   # BankAccount class and BalanceException
├── main.py           # Entry point — creates accounts and runs example transactions
└── README.md
```

## Requirements

- Python 3.x (no external libraries needed)

## How to Run

1. Clone the repository:
   ```
   git clone https://github.com/<your-username>/banking-system-oop.git
   cd banking-system-oop
   ```

2. Run the main script:
   ```
   python main.py
   ```

## Example Usage

```python
from bank_account import *

areej = BankAccount(1000, "Areej")
maryam = BankAccount(2000, "Maryam")

areej.getbalance()
maryam.deposit(500)

maryam.transfer(areej, 500)
```

## Example Output

```
Account 'Areej' created.
 Balance=$1000.00
Account 'Maryam' created.
 Balance=$2000.00

Account 'Areej' has Balance=$1000.00

Deposit complete.

Account 'Maryam' has Balance=$2500.00

==============================

Begining the tranfer...

Withdraw complete.

Account 'Maryam' has Balance=$2000.00

Deposit complete.

Account 'Areej' has Balance=$1500.00

Transfer Complete!

==============================
```

## Concepts Demonstrated

- **Classes & Objects** — modeling real-world entities (bank accounts) as Python objects
- **Encapsulation** — balance and account logic bundled within the `BankAccount` class
- **Custom Exceptions** — `BalanceException` for domain-specific error handling
- **Method Interaction** — `transfer()` reusing `withdraw()` and `deposit()` internally

## Author

Areej