'''Ask the user for a number. Depending on whether the number is even or odd, 
print out an appropriate message to the user. Hint: how does an even / odd 
number react differently when divided by 2?'''

check = int(raw_input("Please give me a number: "))
num = int(raw_input("Please give me another number: "))
if(check % num == 0):
    print("Number " + str(check) + " is divisible by " + str(num))
else:
    print("Number " + str(check) + " is NOT divisible by " + str(num))

