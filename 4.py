class myLife:
  def __init__(self , name = 'han', age = 24 , fav_color =  'Blue'):
    self.name = name 
    self.age = age
    self.fav_color = fav_color 
   
    
  def my_info(self):
      print(f'my name is {self.name} i am {self.age} years old and my favourite color is {self.fav_color}')
 
ml =  myLife('malyun')  
ml.my_info()
mi = myLife('Iqra', 15, 'Black ')
mi.my_info()
mf = myLife('Han', '20', 'white')
myLife.my_info(mf)
