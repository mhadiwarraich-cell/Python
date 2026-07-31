class Vehicle:
    
    
    def __init__(self, max_speed, milage):
        
        
        self.max_speed = max_speed
        self.milage = milage
        
        
modelX = Vehicle(240,18)


print("Model Max Speed:", modelX.max_speed)
print("Moadel Milage :", modelX.milage)