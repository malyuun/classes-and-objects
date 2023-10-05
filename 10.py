class  Laptops:
  def __init__(self,name,ram,core):
    self.name = name
    self.ram = ram
    self.core = core  
    
    
l1= Laptops('dell',8 , 'CORE I3')
print(f'my laptop\'s name is {l1.name} ')
print(f'my laptops is {l1.ram} gb ram')
print(f'my laptops is {l1.core}')

l2 = Laptops('hp',32 , 'CORE I7')
print(f'my laptop\'s name is {l2.name} ')
print(f'my laptops is {l2.ram} gb ram')
print(f'my laptops is {l2.core}')

l3 = Laptops('lenovo',16 , 'CORE I5')
print(f'my laptop\'s name is {l3.name} ')
print(f'my laptops is {l3.ram} gb ram')
print(f'my laptops is {l3.core}')




  
  
  
    
    