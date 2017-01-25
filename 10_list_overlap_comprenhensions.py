#import random
from random import randint, sample

#Generate list A
randomListA = sample(range(20), 10)
print(randomListA)

#Generate list B
randomListB = sample(range(20), 15)
print(randomListB)

coincidenciesList = []
coincidenciesList = [element \
                     for element in randomListA \
                        if (element in randomListB) and (element not in coincidenciesList)]

print(coincidenciesList)
