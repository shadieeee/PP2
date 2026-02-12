class Fly:
    def fly(self):
        return "flying"

class Swim:
    def swim(self):
        return "swimming"

class Duck(Fly, Swim):
    pass

d = Duck()
print(d.fly())
print(d.swim())
class Scroll:
    def scroll(self):
        return "scrolling tiktok"

class Procrastinate:
    def procrastinate(self):
        return "should be studying"

class Me(Scroll, Procrastinate):
    pass

me = Me()
print(me.scroll())
print(me.procrastinate())


class Code:
    def code(self):
        return "writing code"

class Sleep:
    def sleep(self):
        return "sleeping zzz"

class Shai(Code, Sleep):
    pass

me = Shai()
print(me.code())
print(me.sleep())

class Broke:
    def money(self):
        return "0 tenge"

class Shopping:
    def buy(self):
        return "spent on coffee"

class Me(Broke, Shopping):
    pass

me = Me()
print(me.money())
print(me.buy())

class Messages:
    def received(self):
        return "left on read"

class Send:
    def sent(self):
        return "typing..."

class Me(Messages, Send):
    pass

me = Me()
print(me.received())
print(me.sent())