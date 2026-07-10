age = int(input("Enter your age: "))

if age <= 0 or age > 120:
    print("Wrong age entered")
else:
    print("Age is correct")

    if age % 2 == 0:
        print("Age is even")
    else:
        print("Age is odd")