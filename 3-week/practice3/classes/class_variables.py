class Student:
    uni = "KBTU"
    def __init__(self, name):
        self.name = name
        self.points = 0

s1 = Student("Batyr")
s2 = Student("Dias")

s1.points = 77
s2.points = 55

print(s1.uni, s1.name, s1.points)
print(s2.uni, s2.name, s2.points)

Student.uni = "hz"
print(s1.uni, s2.uni)



class Car:
    brand = "Toyota"
    def __init__(self, model):
        self.model = model
        self.speed = 0

c1 = Car("Camry")
c2 = Car("Corolla")

c1.speed = 120
c2.speed = 100

print(c1.brand, c1.model, c1.speed)
print(c2.brand, c2.model, c2.speed)

Car.brand = "Honda"
print(c1.brand, c2.brand)

class Animal:
    kingdom = "Mammal"  # class attribute
    
    def __init__(self, species):
        self.species = species
        self.age = 0

a1 = Animal("Dog")
a2 = Animal("Cat")

a1.age = 5
a2.age = 3

print(a1.kingdom, a1.species, a1.age)
print(a2.kingdom, a2.species, a2.age)

Animal.kingdom = "Reptile"
print(a1.kingdom, a2.kingdom)



class Laptop:
    brand = "hp"
    def __init__(self, ram):
        self.ram = ram

l1 = Laptop("8GB")
l2 = Laptop("16GB")
print(l1.brand, l1.ram)
print(l2.brand, l2.ram)

Laptop.brand = "Mac"
print(l1.brand, l2.brand)