'''Ask the user for two numbers: one number to check 
(call it num) and one number to divide by (check). 
If check divides evenly into num, tell that to the user. 
If not, print a different appropriate message.'''

userInput = int(raw_input("Numero: "))

if((userInput % 2) == 0):
    print("El numero es par")
else:
    print("El numero es impar")
