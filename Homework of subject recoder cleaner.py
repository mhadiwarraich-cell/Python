students = {"Alice": "Math", "Bob": "Science", "Charlie": "Math"}

print(students.get("Alice"))

students["David"] = "History"
students["Bob"] = "Biology"

del students["Charlie"]

print("Length:", len(students))

for name, subject in students.items():
    print(name, ":", subject)