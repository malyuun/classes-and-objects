class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}.")

p1 = Person("Alice")
p1.greet()  # Output: Hello, my name is Alice.

p2 = Person("Bob")
p2.greet()  # Output: Hello, my name is Bob.
