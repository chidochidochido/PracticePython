check = int(raw_input("Please give me a number: "))
num = int(raw_input("Please give me another number: "))
if(check % num == 0):
    print("Number " + str(check) + " is divisible by " + str(num))
else:
    print("Number " + str(check) + " is NOT divisible by " + str(num))

