'''
http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

Exercise 2
ODD OR EVEN

Ask the user for a number. Depending on whether the number is even or odd, 
print out an appropriate message to the user. 

Hint: how does an even / odd number react differently when divided by 2?

Extras:
2) Ask the user for two numbers: one number to check (call it num) and 
one number to divide by (check). If check divides evenly into num, tell 
that to the user. If not, print a different appropriate message.
'''

check = int(raw_input("Please give me a number: "))
num   = int(raw_input("Please give me another number: "))

if(check % num == 0):
    print("Number " + str(check) + " is divisible by " + str(num))
else:
    print("Number " + str(check) + " is NOT divisible by " + str(num))