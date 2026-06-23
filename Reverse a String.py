#Input a word or sentence 
string = input("Please enter your own String : ")

string2 = ('')
#loops for printing in reverse
for i in string:
    string2 = i + string2

    print("\nThe Orignal String = ", string)
    print("The Reversed String = ", string2)
