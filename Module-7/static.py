class Shopping:
    cart = [] #class attributr or satatic attirbute
    origin = 'newzeland'

def __init__(self,name,lication):
    self.name = 'chittagong' #instance attribute
    self.location = 'chawkbazar'

def purchase(self,item,price,amount):
    remaining = amount - price
    print(f'Buying: {item} for price: {price} and remaining: {remaining}')

@staticmethod
def multiply(a,b):
    result =  a*b
    print(result)

@classmethod
def time_pass(self,item):
    print('just for time pass not for shopping',item)



basundhara = Shopping('basun dhara','not popular location')
# basundhara.purchase('tops',500,1000)
basundhara.time_pass('tops')
# Shopping.purchase(2,3,3)
Shopping.time_pass('tops') #class method
Shopping.multiply(4*6) #static method
