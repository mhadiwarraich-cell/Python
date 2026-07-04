# Function to calculate the circumference of a circle

def calculate_circumference(radius):
    pi = 3.14159
    return 2 * pi * radius

# Get input from the user
radius = float(input("Enter the radius of the circle: "))

# Calculate and display the circumference
result = calculate_circumference(radius)

print("The circumference of the circle is:", result)