# Example 1

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

# Example 2

x = "awesome"  # that's global var


def myfunc():
    x = "fantastic"
    print("Python is " + x)  # that's local var


myfunc()

print("Python is " + x)

# Example 3

x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# Example 4

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"

# Example 5

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
