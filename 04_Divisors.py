#list all divisors for a given number
number = int(raw_input("Please give me a number to check: "))
divisors = []

for numDivisor in range(1, number):
    if(number % numDivisor == 0):
        divisors.append(numDivisor)
print(divisors)
