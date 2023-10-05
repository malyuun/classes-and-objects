import math
class Calculations:
  def __init__(self, num1 , num2,radius = 2) :
    self.num1 = num1
    self.num2 = num2
    self.radius = radius
  
  def get_area(radius):
    area = radius * radius * math.pi
    print(area)
    
  def Addition(self):
    print(2 + self.num1 + self.num2)
  
  def Subtraction( x , y):
    print (x - y)
  
  def Division(  x , y):
    print (y / x)
  
  def Multiplication( a, b):
    print(a * b)
    
    

Calculations.get_area(2)

a = Calculations(2,2)
a.Addition()

Calculations.Subtraction(10 , 3)

Calculations.Division(2, 30)

Calculations.Multiplication(5,5)