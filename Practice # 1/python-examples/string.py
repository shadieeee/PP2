# Example 1

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

# Example 2

b = "Hello, World!"
print(b[:5])

# Example 3

a = "Hello, World!"
print(a.lower())

a = " Hello, World! "
print(a.strip())  # returns "Hello, World!"

a = "Hello, World!"
print(a.upper())

# Example 4

a = "Hello"
b = "World"
c = a + " " + b
print(c)

# Example 5 f strings

age = 36
txt = f"My name is John, I am {age}"
print(txt)
