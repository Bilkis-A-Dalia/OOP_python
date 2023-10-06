# read only -->you can not set the value,value can not be changed
# getter --> get a value of a property through a method.most of the time,you will get the value of a privare attribute
# setter --> set a value of property through a method. Most of the time ,you will set a the value of a private property

class User:
    def __init__(self,name,age,money):
        self._name = name
        self._age = age
        self.__money = money

    #getter without any setter is read only attribute
    @property
    def age(self):
        return self._age
    
    #getter
    @property
    def salary(self):
        return self.__money
    
    @salary.setter
    def salary(self,value):
        if value < 0:
            print('salry can not be negative')
        self.__money +=value
    
dalia = User('Dalia',21,12000)
# print(dalia.__money)
# print(dalia.age())  # method call
print(dalia.age) #property method
print(dalia.salary)
dalia.salary = 4500
print(dalia.salary)