class Phone:
    manufactured = 'china'

    def __init__(self,owner,brand,price): #contructor
        self.owner = owner
        self.brand = brand
        self.price = price

    def send_sms(self,phone,sms):
        text = f'sending to:{phone} {sms}'
        print(text)

my_phone = Phone('dalia','iphone',150000)
print(my_phone.owner,my_phone.brand,my_phone.price)

her_phone = Phone('she','oppo',17000)
print(her_phone.owner,her_phone.brand,her_phone.price)

dad_phone = Phone('abbu','nokia',2000)
print(dad_phone.owner,dad_phone.brand,dad_phone.price)