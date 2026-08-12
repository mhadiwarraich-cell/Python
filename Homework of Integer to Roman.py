class Roman:
    def __init__(self, number):
        self.number = number

    def convert(self):
        values = {10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"}
        result = ""

        for value, symbol in values.items():
            while self.number >= value:
                result += symbol
                self.number -= value

        return result


num = int(input("Enter a number: "))
r = Roman(num)

print("Roman:", r.convert())