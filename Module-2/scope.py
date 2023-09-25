# scope- variable inside the function=local

# global variable
balance = 3000

def buy_things(item,price):
    dream_phone = 'xphone'
    global balance # for local new variable (balance=500)
    print(f'previous balance value', balance)
    balance = balance - price
    print(f'balance after buying {item}',balance)
# print(dream_phone)
buy_things('sunglass',1000)
print('global balance after buy', balance)

numbers =[22,19,19,14,33]
numbers.sort()
print(numbers)