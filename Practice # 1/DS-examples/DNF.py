vars = ["p", "q", "r"]


# Any tables for but with less no, 2 <= varibles <= 4
table = [
    [1, 1, 1, 1],
    [1, 1, 0, 1],
    [1, 0, 1, 1],
    [1, 0, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 0, 1],
    [0, 0, 1, 0],
    [0, 0, 0, 0]
]

dnf_parts = []

for row in table:
    values = row[:-1]
    result = row[-1]

    if result == 1:
        part = []

        for i in range(len(vars)):
            if values[i] == 1:
                part.append(vars[i])
            else:
                part.append("¬" + vars[i])

        dnf_parts.append("(" + " ∧ ".join(part) + ")")

dnf = " ∨ ".join(dnf_parts)

print("=" * 70)
print("INPUT")

header = " | ".join(vars) + " | result"
print("  " + header)
print("  " + "-" * len(header))

for row in table:
    print("  " + " | ".join(str(x) for x in row))

print("=" * 70)

print("OUTPUT")
print("- DNF:")
print("  ", dnf)
print("=" * 70)
