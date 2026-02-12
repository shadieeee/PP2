# lambda add
add = lambda a, b: a + b

# lambda double
double = lambda x: x * 2

print(add(2, 3))
print(double(10))
x = lambda a : a + 10
print(x(5))


def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))