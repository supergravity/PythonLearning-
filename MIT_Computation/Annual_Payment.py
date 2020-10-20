
#Initialization

balance = 4773
annualInterestRate = 0.2

#debt = balance*(1 + annualInterestRate)
debt = balance

Monthly_interest_rate = (annualInterestRate/12)


# Main Code

#Guess 1
#balance = balance * (1 + annualInterestRate)
#average_payment = balance / 12

Minimum_monthly_payment = 0
#payment_sum = 0
unpaid_balance = debt

#Guess 2 
while (unpaid_balance >= 0):

    Minimum_monthly_payment += 10
    unpaid_balance = debt
    payment_sum = 0
    for month in range(12):

        #while(Minimum_monthly_payment <= balance):
        unpaid_balance = unpaid_balance - Minimum_monthly_payment
        if(unpaid_balance <= 0):
            break
       unpaid_balance = unpaid_balance * (1+Monthly_interest_rate)
        payment_sum += Minimum_monthly_payment

print("The initial debt is = " + str(debt))

print("The annual balance = " + str(unpaid_balance))
print("The monthly minimum payment = " + str(Minimum_monthly_payment))
