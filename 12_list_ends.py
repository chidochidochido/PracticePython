'''
http://www.practicepython.org/exercise/2014/04/25/12-list-ends.html

EXERCISE 12
LIST ENDS

Write a program that takes a list of numbers 
(for example, a = [5, 10, 15, 20, 25]) and makes 
a new list of only the first and last elements of 
the given list. For practice, write this code inside 
a function.
'''
####################################################
#     GLOBAL VARIABLES
####################################################
a = [5, 10, 15, 20, 25]
outputList = []

#################################################
#    FUNCTION DEFINITIONS
#################################################
def getFirstAndLastElementFromList(inputList):
    outputList.append(inputList[0])
    outputList.append(inputList[-1])

#################################################
#    MAIN PROGRAM
#################################################

#MAIN PROCESSING
getFirstAndLastElementFromList(a)

#OUTPUT
print(outputList)
