class Person:
    name = ""
    age = 0
    city = ""

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("City:", self.city)

p1 = Person()
p1.name = "Rahul"
p1.age = 20
p1.city = "Kolkata"
p1.display()

p2 = Person()
p2.name = "Karan"
p2.age = 22
p2.city = "Bangalore"
p2.display()

