'''
http://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html

EXERCISE 13
FIBONACCI

Write a program that asks the user how many Fibonnaci numbers 
to generate and then generates them. Take this opportunity to 
think about how you can use functions. 

Make sure to ask the user to enter the number of numbers in 
the sequence to generate. (Hint: The Fibonnaci seqence is a 
sequence of numbers where the next number in the sequence is 
the sum of the previous two numbers in the sequence. The 
sequence looks like this: 1, 1, 2, 3, 5, 8, 13, ...)
'''

#################################################
#    FUNCTION DEFINITIONS
#################################################
def Fibonacci(numbersToGenerate):
    #VARIABLE DEFINITIONS / INITIALIZATIONS
    global outputList
    
    #MAIN PROCESSING
    if numbersToGenerate == 1 or numbersToGenerate == 2:
        result = 1;
    else:
        result = Fibonacci(numbersToGenerate -1) + Fibonacci(numbersToGenerate -2)

    #OUTPUTS
    outputList[numbersToGenerate - 1] = result
    return result

#################################################
#    MAIN PROGRAM
#################################################

#VARIABLE DEFINITIONS / INITIALIZATIONS
outputList = [None] * inputNumbersToGenerate

#GET INPUTS
inputNumbersToGenerate = int(raw_input("How many Fibonacci numbers to generate: "))

#MAIN PROCESSING
Fibonacci(inputNumbersToGenerate)

#OUTPUTS
print("Result: ", outputList)
