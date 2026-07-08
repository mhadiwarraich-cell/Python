bill = float(input("Enter bill amount: "))
paid = float(input("Enter paid amount: "))

due = bill - paid

if due > 0:
    print("Due amount:", due)
elif due == 0:
    print("No due. Bill fully paid.")
else:
    print("Change to return:", -due)