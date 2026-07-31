class Parrot:
    
    
    species = "bird"
    
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        
Mithu = Parrot("Mithu", 50)
Chintu = Parrot("Chintu", 40)


print("Mithu is a {}".format(Mithu.species))
print("Chintu is also a {}".format(Chintu.species))


print("{} is{} years old".format( Mithu.name, Mithu.age))
print("{} is{} years old".format( Chintu.name, Chintu.age))