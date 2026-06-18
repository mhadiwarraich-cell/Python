# Enter three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Before swapping:")
print("a =", a)
print("b =", b)
print("c =", c)

# Swapping
a, b, c = c, a, b

print("After swapping:")
print("a =", a)
print("b =", b)
print("c =", c)