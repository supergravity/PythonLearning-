#Using bisection algorithm to guess the number

#Initialization

low_bound = 0 
high_bound = 100
ans = int((high_bound+low_bound)/2)

hint = 0

#Main Part

print("Please think of a number between 0 and 100!")

while (hint != 'c'):

    print("Is your secret number " + str(ans) +" ?")
    print("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.",end=' ')
    

    hint = input()
    #print(hint)

    if(hint == 'h'):
        high_bound = ans
        ans = int((high_bound + low_bound)/2)

    elif(hint == 'l'):
        low_bound = ans
        ans = int((high_bound + low_bound)/2)
    
    elif(hint == 'c'):
        break 

    else:
        print("Sorry, I did not understand your input.")


print("Game over. Your secret number was: " + str(ans))
