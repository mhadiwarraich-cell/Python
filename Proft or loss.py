actual_cost = float(input("please enter your product price be honest: "))
sale_amount = float(input("please enter the sales price: "))
 
if(sale_amount > actual_cost):
    amount = sale_amount - actual_cost
    print("Congrtulations your Total proft ={0}".format(amount))
else:
    print("No profit ok!!!!!!!!")

 