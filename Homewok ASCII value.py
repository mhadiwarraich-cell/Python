# ASCII Value Checker

character = input("Enter a character: ")

if len(character) == 1:
    print("The ASCII value of", character, "is", ord(character))
else:
    print("Please enter only one character.")