class Bank:
    def __init__(self,balance):
        self.balance = balance
        self.min_withdraw = 100
        self.max_withdraw = 100000

    def get_balance(self):
        return self.balance
    
    def deposite(self,amount):
        if amount>0:
            self.balance += amount

    def withdraw(self,amount):
        if amount<self.min_withdraw:
            print (f'you cant withdraw {self.min_withdraw}')
        elif amount>self.max_withdraw:
            print (f'you cant withdraw more than {self.max_withdraw}')
        else:
            self.balance -=amount
            print (f'here is your money {amount}')
            print(f'your balance after withdraw {self.get_balance()}')

brac = Bank(15000)
brac.withdraw(25)
brac.withdraw(50000000)
brac.withdraw(1000)

dbbl = Bank(5000)
dbbl.deposite(2000)
dbbl.deposite(2000)
print(dbbl.get_balance())