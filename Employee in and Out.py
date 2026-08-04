class Employee:
    
    
    def __init__(self):
        print('Employee created')
        
        
        def __del__(self):
            print("Destructor called")
            
            
def Create_obj():
    print('Making Object....')
    onj = Employee()
    print('finction end.....')
    return object

print('Calling Create_obj() function...')
obj = Create_obj()
print('Programe end......')