'''
Ask the user for a number and determine whether the number is 
prime or not. (For those who have forgotten, a prime number is 
a number that has no divisors.). You can (and should!) use your 
answer to Exercise 4 to help you. Take this opportunity to 
practice using functions, described below.
'''

def IsNumberPrime(InputNumber):
    primeNumber = True
    for divisor in range(2, InputNumber):
        if(InputNumber % divisor == 0):
            primeNumber = False
            break
    return primeNumber

UserInput = int(raw_input("Give me a number: "))
primeNumberFlag = IsNumberPrime(UserInput)

if(primeNumberFlag == True):
    print("Number is prime")
else:
    print("Number is not prime")
