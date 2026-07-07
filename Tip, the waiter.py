def total_calc(bill_amount,tip_perc):
#definate function to calculate the tip on bill
    total = bill_amount*(1 + 0.01*tip_perc)
    total = round(total,2)
    print(f"plese pay ${total}")
    
total_calc(150,20)    