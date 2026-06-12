hight = float(input("Wright your hight in the cm stands for cente meter: "))
weight = float(input("Wright yourweight in the KG stands for Kilograms: "))

BMI = weight / (hight/100)**2

print("your BMI is", BMI)

if BMI <= 18.4:
    print("you are safe means under weight.")
elif BMI <= 24.9:
    print("you are safe means healthy.")
elif BMI <= 29.9:
    print("you are unsafe means over weigt.")
elif BMI <= 34.9:
    print("you are very unsafe means severely over weight.")
elif BMI <= 39.9:
    print("you are alot unsafe means obese.")
else:
    print("you are totally unsafe loose your weight right now means severely obse.")