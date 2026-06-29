class BankAccount:
    def __init__(self,acc_holdr_name,balance):
        self.name = acc_holdr_name
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print("Deposited :",amount)
    
    def credit(self,amount):
        if amount > self.balance:
            print("Oops you cant take that much sorry T-T")
            print("Your current balance is : ", self.balance)
        else:
            self.balance -= amount
    
    def showBalance(self):
        return self.balance
    
us1 = BankAccount("Nick",1000)
us1.credit(1000)
us1.deposit(1928377)
print(us1.showBalance())