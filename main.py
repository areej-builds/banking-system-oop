from bank_accounts import *


Areej = BankAccount(1000,"Areej")
Maryam = BankAccount(2000,"Maryam")


Areej.getbalance()
Maryam.deposit(500)

Areej.withdraw(10000)
Areej.withdraw(100)

Maryam.transfer(Areej,500)

Jim = InterestRewardAcc(1000,"Jim")
Jim.getbalance()
Jim.deposit(100)
Jim.transfer(Maryam,500)