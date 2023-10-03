# base class,parent class,common attribute+ functionality class
# derived class, child classcuncommon attribute+ functionality class   


class Device:
    def __init__(self,brand,price,color,origin):
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin
    
    def run(self):
        return f'Running laptop: {self.brand}'
    

class laptop:
    def __init__(self,memory,ssd):
        self.memory = memory
        self.ssd = ssd

    def coding(self):
        return f'Learnig python and practicing'
    
class Phone(Device):
    def __init__(self,brand,price,color,origin,dual_sim):
        self.dual_sim = dual_sim
        super().__init__(brand,price,color,origin)

    def phone_cell(self,number,text):
        return f'Sending SMS to: {number} with {text}'
    
    def __repr__(self):
        return f'phone: {self.brand} {self.price} {self.dual_sim}'
    

class Camera:
    def __init__(self,pixel):
        self.pixel =pixel

    def change_lens(self):
        pass



# inheritance
my_phone = Phone('iphone',1200000,'silver','chine',True)
# my_phone.phone_cell()
print(my_phone.brand)
print(my_phone)
