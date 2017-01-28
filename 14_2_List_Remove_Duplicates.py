'''
http://www.practicepython.org/exercise/2014/05/15/14-list-remove-duplicates.html

EXERCISE 14
List Remove Duplicates

Write a program (function!) that takes a list and returns a new list that contains 
all the elements of the first list minus all the duplicates.

Extras:
1) Write two different functions to do this - one using a loop and constructing a 
list, and another using sets.
'''

initialList = [1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 4, 4, 5, 5, 5]

def removeDuplicates(listWithDuplicates):
    tempListWithoutDuplicates = set(listWithDuplicates)
    return tempListWithoutDuplicates

listWithoutDuplicates = removeDuplicates(initialList)

print("Initial List: " + str(initialList))
print("List Without Duplicates: " + str(listWithoutDuplicates))