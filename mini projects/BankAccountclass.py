class BankAccount:
    def __init__(self,acc_holdr_name,balance):
        self.name = acc_holdr_name
        self.balance = balance

    def deposit(self,amount):
        self.amount = amount
        self.balance += self.amount
    
    def credit(self,amount):
        self.amount = amount
        self.balance -= self.amount
    
    def showBalance(self):
        return self.balance
    
us1 = BankAccount("Nick",100000000)
us1.credit(1928377)
us1.credit(100000000)
us1.deposit(1928377)
print(us1.showBalance())