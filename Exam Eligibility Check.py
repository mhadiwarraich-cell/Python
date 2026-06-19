medical_cause = input("Did you have a medical cause? (Y/N): ").strip().upper() 

if medical_cause == 'Y': 
    print("you are allowed")
else:
    atten = int(input("Enter the attendence of student: "))

    if atten >= 75: 
        print("Aproved")
    else:
        print("Disaproved kock him out")