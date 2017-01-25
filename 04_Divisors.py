'''
http://www.practicepython.org/exercise/2014/02/26/04-divisors.html

EXERCISE 4
DIVISORS

Create a program that asks the user for a number and then prints 
out a list of all the divisors of that number. (If you don?t know 
what a divisor is, it is a number that divides evenly into another 
number. For example, 13 is a divisor of 26 because 26 / 13 has no 
remainder.)

'''
divisors = []

number = int(raw_input("Please give me a number to check: "))

for numDivisor in range(1, number):
    if(number % numDivisor == 0):
        divisors.append(numDivisor)

print(divisors)