'''
http://www.practicepython.org/exercise/2014/01/29/01-character-input.html

Exercise 1
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that 
they will turn 100 years old.'''

#################################################
#    LIBRARIES
#################################################
import datetime


#################################################
#    MAIN PROGRAM
#################################################

#VARIABLE INITIALIZATION
now = datetime.datetime.now()

#GET USER INPUTS
name = raw_input("Give me your name: ")
age  = raw_input("Hi " + name + "! Please give me your age: ")

#MAIN PROCESSING
years_to_100 = 100 - int(age)

#OUTPUT
print("In " + str(now.year + years_to_100) + " you will be 100 years old!")