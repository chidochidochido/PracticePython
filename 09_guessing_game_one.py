'''Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they
guessed too low, too high, or exactly right. (Hint: remember to
use the user input lessons from the very first exercise)'''

from random import randint

continuePlaying = 'yes'

while (continuePlaying != 'exit'):
    generatedNumber = randint(1, 9)
    userInput = int(raw_input("Try to guess the number I have: "))
    attemptsCounter = 1;
    while(userInput != generatedNumber):
        print("Your input: " + str(userInput))
        if(userInput < generatedNumber):
            userInput = int(raw_input("Too low! Try again: "))
        elif(userInput > generatedNumber):
            userInput = int(raw_input("Too high! Try again: "))
        attemptsCounter = attemptsCounter + 1;
    print("Congratulations! Number is " + str(userInput))
    print("# of attempts: " + str(attemptsCounter))
    continuePlaying = input("Play again? (\"exit\" to leave): ")
