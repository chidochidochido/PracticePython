'''
http://www.practicepython.org/exercise/2014/02/15/03-list-less-than-ten.html

EXERCISE 3
LIST LESS THAN TEN

Take a list, say for example this one:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that are less than 5.

Extras:
3) Ask the user for a number and return a list that contains only elements from the 
   original list a that are smaller than that number given by the user.
'''

a = [1, 1, 30, 3, 2, 5, 8, 13, 21, 34, 55, 89]
b = []

number = int(raw_input("Give me a number: "))

#prints out all the elements of the list that are less than 5

for element in a:
    if element < number:
        b.append(element)

print(b)
