a = input()
b = ""

for i in a:
    if i.isdigit():
        print(i)
        b.join(i)

print(b)
