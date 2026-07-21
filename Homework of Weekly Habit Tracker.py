habit = ("Drink Water", "Health", 7)
week = (1, 1, 0, 1, 1, 0, 1)

print(habit)
print(week)
print("Length:", len(week))
print("First habit:", habit[0])
print("Monday:", week[0])
print("Mon-Wed:", week[0:3])
print("Completed:", sum(week))

try:
    week[2] = 1
except TypeError as e:
    print("Error:", e)