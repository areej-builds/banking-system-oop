from bank_accounts import *

'''
Create two regular BankAccount objects
'''
Areej = BankAccount(1000,"Areej")
Maryam = BankAccount(2000,"Maryam")


Areej.getbalance()
Maryam.deposit(500)

'''
Try to withdraw more than the balance -> should fail gracefully,
then do a valid withdrawal
'''
Areej.withdraw(10000)
Areej.withdraw(100)

'''
Transfer money from Maryam to Areej
'''
Maryam.transfer(Areej,500)

'''
Create an InterestRewardAcc -> deposits get a 5% bonus,
then transfer from Jim to Maryam
'''
Jim = InterestRewardAcc(1000,"Jim")
Jim.getbalance()
Jim.deposit(100)
Jim.transfer(Maryam,500)

'''
Create a SavingAcc -> gets the 5% deposit bonus + a withdrawal fee,
then transfer from Fatima to Jim
'''
Fatima = SavingAcc(1000,"Fatima")
Fatima.getbalance()
Fatima.deposit(100)
Fatima.transfer(Jim,200)

'''
Test: try to transfer more than Jim's (InterestRewardAcc) balance -> should fail gracefully
'''
Jim.transfer(Maryam,10000)

'''
Test: try to transfer more than Fatima's (SavingAcc) balance -> should fail gracefully
'''
Fatima.transfer(Jim,10000)