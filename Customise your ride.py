print("Slect your ride: ")
print("Our dangrous ride the Cricle Rolarcoster 1.")
print("Our 2 most popular ride is iceskating 2.")

#take input of number 1 or 2
#slect your ride
choice = int(input("Enter your choice: ") )

#User entring option 1
if( choice == 1 ): #condition 1 outer if statement
    print( "What type of Rolar costor" )
    print("1.full circle\n")
    print("less cicle\n")

    #condition for slecting the tupe of rolarcoster
    choice2=int(input("`Enter your choice2: "))
    if choice2==1: #inner if sttatement
        print("ypu have slected full circle")
    else:
        print("you have slected less circle")
        
#user entering option 2
elif( choice == 2 ): #outer elif stetement
    print("What type of iceskating")
    print("1.more snoe and slides")
    print("2. less snow but they are slides")
    choice3=int(input("enter your choice3: "))

    if choice3==1: #inner if statement
        #condition for slecting the type of iceskating
           print("you have slected more snow and slides")
    else:   
         print("you have slected less snow but there is slides")

else: #outer else statement 
     print("You are not ready for that Wrong Choice!")
        



