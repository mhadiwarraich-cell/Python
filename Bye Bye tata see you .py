valid = False 
while not valid:
    try:
        n=int(input("Enter a number: "))
        
        while n%2==0:
            print("bye bye tata see you never see you again in my entire life")
        valid = True
    except ValueError:
        print("Indvalid")