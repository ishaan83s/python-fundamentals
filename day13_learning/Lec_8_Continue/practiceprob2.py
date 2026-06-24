#Create account class with 2 attributes - balance and account no
#Create methods for debit , credit and printing the balance

class Account:
    def __init__(self,balance , account_no):
        self.balance = balance
        self.account_no = account_no
    
    def debit(self,amount):
        self.balance -= amount
        print(amount," Rs was debited")
        print("total balance : ",self.get_balance())
    
    def credit(self,amount):
        self.balance += amount
        print(amount," Rs was credited")
        print("total balance : ",self.get_balance())

    def get_balance(self):
        return (self.balance)



s1 = Account(1500,1)
s1.credit(1000)
