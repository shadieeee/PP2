class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, group):
        super().__init__(name)
        self.group = group

s = Student("shadieeee", "site")
print(s.name, s.group)

class Drink:
    def __init__(self, name):
        self.name = name

class Coffee(Drink):
    def __init__(self, name, caffeine):
        super().__init__(name)
        self.caffeine = caffeine

d = Coffee("latte", "high")
print(d.name, d.caffeine)

class Pet:
    def __init__(self, name):
        self.name = name

class Cat(Pet):
    def __init__(self, name, mood):
        super().__init__(name)
        self.mood = mood

c = Cat("merry", "cuddling")
print(c.name, c.mood)

class Employee:
    def __init__(self, name):
        self.name = name

class Boss(Employee):
    def __init__(self, name, bonus):
        super().__init__(name)
        self.bonus = bonus

b = Boss("nnn", "1000")
print(b.name, b.bonus)