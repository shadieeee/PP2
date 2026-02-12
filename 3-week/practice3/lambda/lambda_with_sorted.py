students = [
    {"name": "Dias", "score": 98, "time": 13, "ratio": 0.7},
    {"name": "shadie", "score": 99, "time": 10, "ratio": 0.9},
    {"name": "Dimash", "score": 97.5, "time": 23, "ratio": 0.8},
]

# sort score
by_score = sorted(students, key=lambda s: s["score"])
by_name = sorted(students, key=lambda s: s["name"])
bu_time = sorted(students, key=lambda s: s["time"], reverse=True)

byratio = sorted(students, key=lambda s: s["ratio"])

print(by_score)
print(by_name)
print(bu_time)
print(byratio)