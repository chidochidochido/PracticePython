# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
# and makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function.

a = [5, 10, 15, 20, 25]
outputList = []

def getFirstAndLastElementFromList(inputList):
    outputList.append(inputList[0])
    outputList.append(inputList[-5])

getFirstAndLastElementFromList(a)
print(outputList)
