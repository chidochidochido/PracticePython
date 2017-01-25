#import random
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
