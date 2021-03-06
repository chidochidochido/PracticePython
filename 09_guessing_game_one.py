'''
http://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

EXERCISE 9
GUESSING ONE GAME

Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they
guessed too low, too high, or exactly right. (Hint: remember to
use the user input lessons from the very first exercise)

Extras:
1) Keep the game going until the user types "exit"
2) Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''

from random import randint

continuePlaying = 'yes'

while (continuePlaying != 'exit'):
    attemptsCounter = 1;
    generatedNumber = randint(1, 9)
    
    userInput = int(raw_input("Try to guess the number I have: "))
    
    while(userInput != generatedNumber):
        print("Your input: " + str(userInput))
        
        if(userInput < generatedNumber):
            userInput = int(raw_input("Too low! Try again: "))
        elif(userInput > generatedNumber):
            userInput = int(raw_input("Too high! Try again: "))
        
        attemptsCounter = attemptsCounter + 1;
    
        
    print("Congratulations! Number is " + str(userInput))
    print("# of attempts: " + str(attemptsCounter))
    
    
    continuePlaying = raw_input("Play again? (\"exit\" to leave): ")