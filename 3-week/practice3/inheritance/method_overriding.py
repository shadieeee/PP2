class Vehicle:
    def move(self):
        return "moves"

class Car(Vehicle):
    def move(self):
        return "drives"

v = Vehicle()
c = Car()
print(v.move())
print(c.move())
class Student:
    def work(self):
        return "studying"

class Shai(Student):
    def work(self):
        return "rotting"

s = Student()
me = Shai()
print(s.work())
print(me.work())

class ppl:
    def do(self):
        return "breathing"

class Shai(ppl):
    def do(self):
        return "hzzzzzzzzzz"

p = ppl()
im= Shai()
print(p.do())
print(im.do())