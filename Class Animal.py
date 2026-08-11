from abc import ABC,abstractmethod

class Animal(ABC):
    
    
    def move(self):
        pass
    
class Human(Animal):
    def move(self):
        print("I can walk and run and gaming")
        
        
class Snake(Animal):
        
        def move(self):
            print("I can Crawel and nagin dance")
            
class Dog(Animal):
    
    def move(self):
        print("Mera kam bhonkna ha")
        
class Lion(Animal):
    
    def move(self):
        print("I can scare everyone ")
        















C = Human()
C.move()


R = Snake()
R.move()


H = Dog()
H.move()


W = Lion()
W.move()