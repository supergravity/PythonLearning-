#Initialization

#balance = 0
#annualInterestRate = 0
#monthlyPaymentRate = 0
balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
print("balance = " + str(balance))
print("annualInterestRate = " + str(annualInterestRate))
print("monthlyPaymentRate = " + str(monthlyPaymentRate))



for month in range (12):
    Monthly_interest_rate = (annualInterestRate / 12.0) 
    Minimum_monthly_payment = monthlyPaymentRate*balance
    Monthly_unpaid_balance  = balance - Minimum_monthly_payment
    balance = (Monthly_unpaid_balance) + (Monthly_interest_rate * Monthly_unpaid_balance)
    print("Month " + str(month+1) + " Remaining balance: " + str(balance))

balance = round(balance,2)

print("Remaining balance: " + str(balance))






