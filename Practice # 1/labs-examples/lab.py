# 1 Example

a = input()
print(f"Hello, {a}")

# 2 Example

a = input()
b = input()

print(f"{a}***{b}")

# 3 Example

a = str(input())

if a.isdigit():
    print("int")
else:
    print("str")

# 4 Example

a = input()
b = input()

print(a + b)

# 5 Example

a = input()
b = input()

print(a // b)
print(a / b)

# 6 Example

a = input()
b = input()

print(a**b)

# 7 Example

a = input()
b = input()

print(a % b)

# 8 Example

a = str(input())
b = input()

print(a*b)

# 9 Example

a = input()
print(len(a))

# 10 Example

a = input()
print(a.upper())
print(a.lower())


# 11 Example

a = input()
if len(a) == 1:
    print(f"{a} {a}")
else:
    print(f"{a[0]} {a[-1]}")

# 12 Example

a = input()

print(f"{a[2:5]}")

# 13 Example

a = input()
b = reversed(a)

print("".join(b))

# 14 Example

a = input()
b = input()

print(f"Hello, {a}. You are {b} years old.Hello, Alice. You are 30 years old.")

# 15 Example

a = input()
b = input()

if b in a:
    print("True")
else:
    print("False")

# 16 Example

a = input()
b = input()

print(f"{a}{b}")

# 17 Example

a = input()
b = input()

print(f"{b} {a}")

# 18 Example

a = input()

if a % 2 == 0:
    print("even")
else:
    print("odd")

# 19 Example

a = input()
b = input()
c = input()

print(a.replace(b, c))

# 20 Example

a = input()
b = input()

if a > b:
    print(a)
elif b > a:
    print(b)
else:
    print("equal")
