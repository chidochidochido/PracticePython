'''
http://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

Exercise 2
ODD OR EVEN

Ask the user for a number. Depending on whether the number is even or odd, 
print out an appropriate message to the user. 

Hint: how does an even / odd number react differently when divided by 2?
'''

userInput = int(raw_input("Numero: "))

if((userInput % 2) == 0):
    print("El numero es par")
else:
    print("El numero es impar")
