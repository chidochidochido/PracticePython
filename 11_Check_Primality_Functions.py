'''
http://www.practicepython.org/exercise/2014/04/16/11-check-primality-functions.html

EXERCISE 11
CHECK PRIMALITY FUNCTIONS

Ask the user for a number and determine whether the number is 
prime or not. (For those who have forgotten, a prime number is 
a number that has no divisors.). You can (and should!) use your 
answer to Exercise 4 to help you. Take this opportunity to 
practice using functions, described below.
'''

#################################################
#    FUNCTION DEFINITIONS
#################################################
def IsNumberPrime(InputNumber):
    primeNumber = True
    
    for divisor in range(2, InputNumber):
        if(InputNumber % divisor == 0):
            primeNumber = False
            break

    return primeNumber

#################################################
#    MAIN PROGRAM
#################################################

#INPUT
UserInput = int(raw_input("Give me a number: "))

#MAIN PROCESSING
#OUTPUT
primeNumberFlag = IsNumberPrime(UserInput)
if(primeNumberFlag == True):
    print("Number is prime")
else:
    print("Number is not prime")