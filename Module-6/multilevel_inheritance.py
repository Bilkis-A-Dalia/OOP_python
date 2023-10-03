class vehicle:
    def __init__(self,name,price):
        self.name= name
        self.price =price

    def __repr__(self):
        return f'{self.name} {self.price}'

    def move(self):
        pass

class Bus(vehicle):
    def __init__(self,name,price,seat):
        self.seat = seat
        super().__init__(name,price)

    def __repr__(self):
        return super().__repr__()

    

class Track(vehicle):
    def __init__(self,name,price,weight):
        self.weight = weight
        super().__init__(name,price)

class PickupTrack(Track):
    def __init__(self,name,price,weight):
        super().__init__(name,price,weight)

class AcBus(Bus):
    def __init__(self,name,price,seat,temp):
        self.temp = temp
        super().__init__(name,price,seat)

    def __repr__(self):
        print(f'{self.seat}')
        return super().__repr__()

green_line = AcBus('green',5000000,22,16)
print(green_line)
