'''
http://www.practicepython.org/exercise/2014/04/10/10-list-overlap-comprehensions.html

EXERCISE 10
LIST OVERLAP COMPRENHENSIONS

This week's exercise is going to be revisiting an old exercise (see Exercise 5), 
except require the solution in a different way.

Take two lists, say for example these two:
	a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
	b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that are 
common between the lists (without duplicates). Make sure your program works on two 
lists of different sizes. Write this in one line of Python using at least one list 
comprehension. (Hint: Remember list comprehensions from Exercise 7).

The original formulation of this exercise said to write the solution using one line 
of Python, but a few readers pointed out that this was impossible to do without using 
sets that I had not yet discussed on the blog, so you can either choose to use the 
original directive and read about the set command in Python 3.3, or try to implement 
this on your own and use at least one list comprehension in the solution.

Extra:
1) Randomly generate two lists to test this
'''


#import random
from random import randint, sample

coincidenciesList = []

#Generate list A
randomListA = sample(range(20), 10)
print(randomListA)

#Generate list B
randomListB = sample(range(20), 15)
print(randomListB)


coincidenciesList = [element \
                     for element in randomListA \
                        if (element in randomListB) and (element not in coincidenciesList)]


print(coincidenciesList)