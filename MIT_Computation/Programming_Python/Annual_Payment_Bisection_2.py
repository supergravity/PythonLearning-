#Using bisection algorithm to pinpoint the minimum Monthly Payment

#Initialization

balance = 999999
#balance = 320000

annualInterestRate = 0.18
#annualInterestRate = 0.20


Monthly_interest_rate = annualInterestRate / 12
Monthly_payment_lower_bound = balance / 12
Monthly_payment_upper_bound = (balance * (1 + Monthly_interest_rate)**12) / 12.0

rate = (1+ Monthly_interest_rate)


Minimum_monthly_payment = (Monthly_payment_lower_bound + Monthly_payment_upper_bound)/2
total_Payment = Minimum_monthly_payment * (1 - (rate)**12)/(1 - rate)
actual_debt = balance * (rate ** 11)

check_balance = total_Payment - actual_debt

steps = 0

#while (abs(check_balance) > 2):
while (abs(check_balance) != 0):



    if (check_balance < 0):
        Monthly_payment_lower_bound = Minimum_monthly_payment
        Minimum_monthly_payment = (Monthly_payment_lower_bound + Monthly_payment_upper_bound)/2

    elif (check_balance > 0):
        Monthly_payment_upper_bound = Minimum_monthly_payment
        Minimum_monthly_payment = (Monthly_payment_lower_bound + Monthly_payment_upper_bound)/2


    total_Payment = Minimum_monthly_payment * (1 - (rate)**12)/(1 - rate)
    check_balance = total_Payment - actual_debt
#
#    print("The actual debt is : " + str(actual_debt))
#    print("The total_Payment is : " + str(total_Payment))
#    print("The check_balance is : " + str(check_balance))
#    print("Minimum_monthly_payment test: " + str(Minimum_monthly_payment))
    steps += 1
Minimum_monthly_payment = round(Minimum_monthly_payment,2)

print("steps of guessing: " + str(steps))
print("The actual debt is : " + str(actual_debt))
print("The total_Payment is : " + str(total_Payment))
print("The check_balance is : " + str(check_balance))
print("The minimum monthly payment is : " + str(Minimum_monthly_payment))




