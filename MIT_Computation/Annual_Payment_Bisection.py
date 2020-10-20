#Using bisection algorithm to pinpoint the Minimum Monthly Payment

#Initialization


#balance = 320000
balance = 999999
#annualInterestRate = 0.2
annualInterestRate = 0.18

Monthly_interest_rate = annualInterestRate / 12
Monthly_payment_lower_bound = balance / 12
Monthly_payment_upper_bound = (balance * (1 + Monthly_interest_rate)**12) / 12.0

debt = balance
unpaid_balance = debt


while(unpaid_balance >= 0):

    Minimum_monthly_payment = (Monthly_payment_lower_bound + Monthly_payment_upper_bound)/2
    unpaid_balance = debt
    #payment_sum = 0
    #total_debt  = debt
    for month in range (12):

        unpaid_balance = unpaid_balance - Minimum_monthly_payment
        #payment_sum += Minimum_monthly_payment
        #total_debt  += unpaid_balance
        print("The unpaid_balance of month " + str(month+1) + " is " + str(unpaid_balance))
        #print("The payment_sum of month " + str(month+1) + " is " + str(payment_sum))
        if (unpaid_balance <= 0):
           break
        unpaid_balance = unpaid_balance * (1+Monthly_interest_rate)

    if ():
        Monthly_payment_lower_bound = Minimum_monthly_payment
    elif ():
        Monthly_payment_upper_bound = Maximum_monthly_payment



Minimum_monthly_payment = round(Minimum_monthly_payment,2)

print("The initial debt is = " + str(debt))
#print("The final debt is = " + str(total_debt))
print("The annual balance = " + str(unpaid_balance))
#print("The total payment = " + str(payment_sum))
print("The monthly minimum payment = " + str(Minimum_monthly_payment))


#Check 

print("========================Check===============================")
rate = (1+Monthly_interest_rate)
check_balance = balance * ((rate)**11) - (Minimum_monthly_payment * (1 - (rate)**12)/(1 - (rate)))
print(str(check_balance))

