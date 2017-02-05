'''
http://www.practicepython.org/exercise/2014/03/05/05-list-overlap.html

EXERCISE 5
LIST OVERLAP

Take two lists, say for example these two:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the 
elements that are common between the lists (without duplicates). 
Make sure your program works on two lists of different sizes.

Extras:
1) Randomly generate two lists to test this
'''

from random import randint

randomListA = []
randomListB = []
coincidenciesList = []

#Generate list a
for counter in range(0, 11):
    number = randint(0, 5)
    randomListA.append(number)
print(randomListA)

#Generate list b
for counter in range(0, 15):
    number =  randint(0, 5)
    randomListB.append(number)
print(randomListB)


for element in randomListA:
    if (element in randomListB) and (element not in coincidenciesList):
        coincidenciesList.append(element)


print(coincidenciesList)