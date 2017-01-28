'''
http://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html

EXERCISE 14
List Remove Duplicates

Write a program (function!) that takes a list and returns a new list that contains 
all the elements of the first list minus all the duplicates.

Extras:
2) Go back and do Exercise 5 using sets, and write the solution for that in a 
different function.

EXERCISE 5
LIST OVERLAP

Take two lists, say for example these two:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the 
elements that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.
'''

#import random
from random import randint

randomListA = []
randomListB = []
listWithElementsInCommon = []
listWithoutDuplicates = []

def createNewListWithElementsInCommon(inputList1, inputList2):
    newListWithElementsInCommon = []
    for list1_element in inputList1:
        if(list1_element in inputList2):
             newListWithElementsInCommon.append(list1_element)
    return newListWithElementsInCommon

def generateRandomList(randomList):
    numberOfElements = randint(10, 15)
    for listIndex in range(0, numberOfElements):
        numberToAppend = randint(0, 5)
        randomList.append(numberToAppend)
    return randomList

generateRandomList(randomListA)
generateRandomList(randomListB)
listWithElementsInCommon = createNewListWithElementsInCommon(randomListA, randomListB)
listWithoutDuplicates = list(set(listWithElementsInCommon))

print("Random List A: " + str(randomListA))
print("Random List B: " + str(randomListB))
print("List with elements in common: " + str(listWithElementsInCommon))
print("List without duplicates: " + str(listWithoutDuplicates))