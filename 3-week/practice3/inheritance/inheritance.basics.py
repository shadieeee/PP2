class Animal:
    def speak(self):
        return "hz"

class Cat(Animal):
    def speak(self):
        return "meow"
class dog(Animal):
    def speak(self):
        return "gaw"
class human(Animal):
    def speak(self):
        return "hello"

a = Animal()
c = Cat()
d=dog()
aa=human()
print(a.speak())
print(c.speak())
print(d.speak())
print(aa.speak())