class Calculator:
    def add(self,a,b):
        return a+b
    def subtract(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def divide(self,a,b):
        if b == 0:
            return "Cannot divide by zero"
        return a/b
# Get user input for a and b
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
    
#create an instance of the Calculator class
calculator = Calculator()
    
#Test the calculator methods
print("Addition: ",calculator.add(a,b))
print("Subtraction: ",calculator.subtract(a,b))
print("Multiplication: ",calculator.multiply(a,b))
print("Division: ",calculator.divide(a,b))
print("Division by zero: ",calculator.divide(a,0))
