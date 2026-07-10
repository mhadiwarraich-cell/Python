try:
    num1,num2, = eval(input("Enter two numbers, separeted by a comma : "))
    result = num1 / num2
    print("Result is", result)
    
    
except    ZeroDivisionError:
    print("Division is failed by 0")
    
except SyntaxError:
    print("Comma is missing. Enter numbers separeted by comma like this 1, 2 ")
    
except:
    print("Wrong input")
    
finally:
    print("This will exicute no woorys")