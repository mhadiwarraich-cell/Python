class Pakistan():
    def capital(self):
        print("Islamabad is the official the capital of pakistan")
        
    def language(self):
        print("Urdu is the most common in PK")
        
    def type(self):
        print("Pakistan is most powerfull country")
        
        
class Turkey():
    def capital(self):
        print("instanbul, is the capital")
        
    def language(self):
        print("turkish")
        
    def type(self):
        print("turkey turist place")
        
        
obj_PK = Pakistan()
obj_Turkey = Turkey()


for country in (obj_PK, obj_Turkey):
    country.capital()
    country.language()
    country.type()