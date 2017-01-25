#Ask the user for a number and determine whether the number is prime or not.
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
