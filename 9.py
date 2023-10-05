class  Laptops:
  def __init__(self,name,ram,core):
    self.name = name
    self.ram = ram
    self.core = core
  
  def laptops_info(self):
    print(f'my laptop is {self.name} and it has {self.ram} and it is {self.core}')
  
  
    
l1= Laptops('dell',8 , 'CORE I3')
l1.laptops_info()
l2 = Laptops('hp',32 , 'CORE I7')
l2.laptops_info()
l3 = Laptops('lenovo',16 , 'CORE I5')
l3.laptops_info()



  
  
  
    
    