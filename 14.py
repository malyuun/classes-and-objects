class Arithmetic:
  def __init__(self,firstNum,secondNum) :
    self.firstNum = firstNum
    self.secondNum =  secondNum
  def getAddition(self):
    return  self.firstNum + self.secondNum
  def setValue(self,firstN,secondN):
    self.firstNum = firstN
    self.secondNum = secondN
    

  
add = Arithmetic(50,50)
print(add.getAddition())
add.setValue(30,4)
print(add.getAddition())
        