'''balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
'''
monthlyInterestRate=annualInterestRate/12.0
paid=0
for i in range(1,13):
    print "Month: " +str(i)
    Total=balance
    change=monthlyPaymentRate*balance
    paid+=change    
    balance=Total-change
    #print "Balance:" +str(Total-change)
        
    print "Minimum monthly payment: " +str(round(monthlyPaymentRate*Total,2))
    
    #print balance    
    balance=balance+monthlyInterestRate*balance    
    print "Remaining balance: " + str(round(balance,2))

    
print "Total paid " + str(round(paid,2))
print "Remaining balance " + str(round(balance,2))
