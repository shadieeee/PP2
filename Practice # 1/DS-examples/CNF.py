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

cnf_parts = []

for row in table:
    values = row[:-1]
    result = row[-1]

    if result == 0:
        part = []

        for i in range(len(vars)):
            if values[i] == 0:
                part.append(vars[i])
            else:
                part.append("¬" + vars[i])

        cnf_parts.append("(" + " v ".join(part) + ")")

cnf = " ∧ ".join(cnf_parts)

print("=" * 70)
print("INPUT")

header = " | ".join(vars) + " | result"
print("  " + header)
print("  " + "-" * len(header))

for row in table:
    print("  " + " | ".join(str(x) for x in row))

print("=" * 70)

print("OUTPUT")
print("- CNF:")
print("  ", cnf)
print("=" * 70)
