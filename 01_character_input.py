import datetime
now = datetime.datetime.now()

name = raw_input("Give me your name: ")
age = raw_input("Hi " + name + "! Please give me your age: ")
years_to_100 = 100 - int(age)
print("In " + str(now.year + years_to_100) + " you will be 100 years old!")
