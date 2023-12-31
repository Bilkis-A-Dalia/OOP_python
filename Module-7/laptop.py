# inheritance vs composition

class CPU:
    def __init__(self,cores) -> None:
        self.cores = cores

class RAM:
    def __init__(self,size) -> None:
        self.size = size

class HardDrive:
    def __init__(self,capacity) -> None:
        self.capacity = capacity


# laptop has a cpu
# laptop has a ram
# laptop has a hard drive
class Laptop:
    def __init__(self,cores,ram_size,hd_capacity) -> None:
        self.cpu = CPU(cores)
        self.ram = RAM(ram_size)
        self.hard_disc = HardDrive(hd_capacity)

mac = Laptop(8,16,512)
