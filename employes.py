class Employee:
  def __init__(self,name,salary,address):
    self.name = name
    self.salary = salary
    self.address =  address
    self.time_in = []
    self.time_out = []

    
  def Time_in(self,time):
    self.time_in.append(time)
  
  def Time_out(self,timeout):
    self.time_out.append(timeout)
    
    
    
emp1 = Employee("safiya", 1000,"km4")
#print(emp1.name)
emp1.Time_in('07')
print(emp1.time_in)
emp1.Time_out('17:00')
print(emp1.time_out)

print(f"{emp1.name} shift start at {emp1.time_in}am and ends {emp1.time_out}pm")



