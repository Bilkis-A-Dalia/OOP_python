class Bank:
    def __init__(self,holder_name,initial_deposit):
        self.holder_name = holder_name #public attribute 
        self._branch = 'bonani 11' #protected
        self.__balance = initial_deposit #private

    def deposit(self,amount):
        self.__balance +=amount

    def get_balance(self):
        return self.__balance
    
    def withdraw(self,amount):
        if amount < self.__balance:
            self.__balance = self.__balance - amount
            return amount
        else:
            return f'empty acount'

dalia = Bank("boro meye",10000)
print(dalia.holder_name)
dalia.holder_name = 'bilkis'
dalia.deposit(4000)
print(dalia.get_balance())
print(dalia.holder_name)
# print(dalia._branch)
# print(dir(dalia))
print(dalia._Bank__balance)