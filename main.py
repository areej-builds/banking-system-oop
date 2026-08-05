from bank_accounts import *

# Create two regular BankAccount objects
Areej = BankAccount(1000,"Areej")
Maryam = BankAccount(2000,"Maryam")


Areej.getbalance()
Maryam.deposit(500)

# Try to withdraw more than the balance -> should fail gracefully
Areej.withdraw(10000)
# Valid withdrawal
Areej.withdraw(100)

# Transfer money from Maryam to Areej
Maryam.transfer(Areej,500)

# Create an InterestRewardAcc -> deposits get a 5% bonus
Jim = InterestRewardAcc(1000,"Jim")
Jim.getbalance()
Jim.deposit(100)
# Transfer from Jim to Maryam
Jim.transfer(Maryam,500)

# Create a SavingAcc -> gets the 5% deposit bonus + a withdrawal fee
Fatima = SavingAcc(1000,"Fatima")
Fatima.getbalance()
Fatima.deposit(100)
# Transfer from Fatima to Jim
Fatima.transfer(Jim,200)