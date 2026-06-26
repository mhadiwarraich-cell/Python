#Take input of word
string = input("Plese enter your own word : ")
#take input for a chractert
char = input("Plese enter your own Chracter : ")
i = 0
count = 0
#loop will to find the occurence
while(i < len(string)): #string opreation

    if(string[i] == char): #condition 1
     count = count + 1
    i = i + 1

#Disblay the result
print("The total Number of Times ", char, "has Occurred = " , count)
    