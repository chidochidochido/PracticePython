a = [1, 1, 30, 3, 2, 5, 8, 13, 21, 34, 55, 89]
b = []

number = raw_input("Give me a number: ")

#prints out all the elements of the list that are less than 5

for element in a:
    if element < int(number):
        b.append(element)

print(b)
