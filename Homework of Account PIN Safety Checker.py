# Account PIN Safety Checker

class Account:
    def __init__(self, pin):
        self.__pin = pin  # Private attribute

    def set_pin(self, new_pin):
        self.__pin = new_pin

    def __str__(self):
        return "Account PIN: ****"

account = Account("1234")

# Try to access private data
try:
    print(account.__pin)
except:
    print("Private PIN cannot be accessed directly.")

# Update PIN using setter
account.set_pin("5678")

# Print object
print(account)