import math

class Circle :
  def __init__(self,radius = 1):
    self.radius = radius
  def getPerimeter(self):
    return 2 * self.radius * math.pi
  def getArea(self):
    return self.radius * self.radius * math.pi
  def  setRadius(self,radius):
    self.radius = radius

circle1 = Circle()
print(circle1.getPerimeter())
circle2 = Circle()
print(circle2.getArea())
circle3 = Circle()
print(circle3.radius)


    
    
    
    