class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def info(self):
        return self.name + " " + str(self.age)

p = Person("shai", 18)
print(p.info())
class Pizza:
    def __init__(self, topping, size):
        self.topping = topping
        self.size = size
    
    def info(self):
        return self.topping + " " + str(self.size) + '"'

p = Pizza("cheese", 12)
print(p.info())

class Song:
    def __init__(self, artist, duration):
        self.artist = artist
        self.duration = duration
    
    def info(self):
        return self.artist + " " + str(self.duration) + "s"

s = Song("akiko", 210)
print(s.info())


class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages
    
    def info(self):
        return self.title + " " + str(self.pages) + "p"

b = Book("hatrry potter", 300)
print(b.info())