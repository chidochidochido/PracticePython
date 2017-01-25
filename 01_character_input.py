'''Create a program that asks the user to enter their name and their age. Print out a 
message addressed to them that tells them the year that they will turn 100 years old.'''

import datetime
now = datetime.datetime.now()

name = raw_input("Give me your name: ")
age = raw_input("Hi " + name + "! Please give me your age: ")
years_to_100 = 100 - int(age)
print("In " + str(now.year + years_to_100) + " you will be 100 years old!")
