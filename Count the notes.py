# Talking total amount as input from user
Amount =int(input("Enter how much money you want from your bank"))
            
# Calculating the number of notes of different denominatores
note_X = Amount//5000
note_A = (Amount%5000)//1000
note_B = ((Amount%5000)%1000)//500
note_C = (((Amount%5000)%1000)%500)//100
note_Y = ((((Amount%5000)%1000)%500)%100)//50
note_R = (((((Amount%5000)%1000)%500)%100)%50)//20
note_P = ((((((Amount%5000)%1000)%500)%100)%50)%20)//5

print("notes of 5000" ,note_X)
print("notes of 1000" ,note_A)
print("notes of 500" ,note_B)
print("notes of 100" ,note_C)
print("note of 50" ,note_Y)
print("note of 20" ,note_R)
print("note of 10" ,note_P)

