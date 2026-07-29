import random
import string

# Letters and numbers
chars = string.ascii_letters + string.digits

# Create an 8-character password
password = ""

for i in range(8):
    password += random.choice(chars)

print("Random Password:", password)