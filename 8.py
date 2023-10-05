class Family:
  def __init__(self,name,age,weight,height,fav_food,fav_color):
    self.name = name
    self.age = age
    self.weight = weight
    self.height = height
    self.fav_food = fav_food
    self.fav_color =fav_color
  
  def members_description(self):
    print(f'my name is {self.name}')
    print(f'{self.name} is {self.age} years old')

    print(f'{self.name}\'s  weight is  {self.weight} kg')

    print(f'{self.name}\'s height is {self.height} cm')

    print(f'{self.name}\'s favourite color is {self.fav_color}')
    print(f'{self.name}\'s favourite food is {self.fav_food}')


  
  
    
member1 = Family('Malyun', 18, 51 , 165,'rice','blue')
member1.members_description()
member2 = Family('Iqra', 15, 49,162,'pasta','green' )
member2.members_description()
member3 = Family('Deeqa',23, '65kg', '170cm','rice','white')
member3.members_description()






