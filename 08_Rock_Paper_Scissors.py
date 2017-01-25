''' 
http://www.practicepython.org/exercise/2014/03/26/08-rock-paper-scissors.html

EXERCISE 8
ROCK PAPER SCISSORS

Make a two-player Rock-Paper-Scissors game.
(Hint: Ask for player plays (using input),compare them, 
print out a message of congratulations to the
winner, and ask if the players want to start a new game)

Remember the rules:
-Rock beats scissors
-Scissors beats paper
-Paper beats rock
'''

from random import randint

validInputs = ('PAPER',
               'ROCK',
               'SCISSORS')

gameStatus = ('WIN',
              'CONTINUE',
              'LOSE')

currentGameStatus = 'CONTINUE'

print("\
Welcome to the Rock-Paper-Scissors game:\
Remember the rules:\n\
   Rock beats scissors\n\
   Scissors beats paper\n\
   Paper beats rock\n")

while(currentGameStatus == 'CONTINUE'):
    #User choice
    userInputInt = int(input("GIVE ME YOUR INPUT (0 - PAPER, 1 - ROCK, 2 - SCISSORS): "))
    userInputEnum = validInputs[userInputInt]
    
    #Computer choice
    computerChoiceInt = randint(0, 2)
    computerChoiceEnum = validInputs[computerChoiceInt]

    #Print both choices
    print("Your input: " + str(userInputEnum))
    print("Computer input: " + str(computerChoiceEnum))

    #Decide whether it's a DRAW, WIN or LOSE
    if(userInputEnum == computerChoiceEnum):
        print("That's a draw!")
    elif(userInputEnum == 'PAPER'):
        if(computerChoiceEnum == 'ROCK'):
            currentGameStatus = 'WIN'
        else:
            currentGameStatus = 'LOSE'
    elif(userInputEnum == 'ROCK'):
        if(computerChoiceEnum == 'SCISSORS'):
            currentGameStatus = 'WIN'
        else:
            currentGameStatus = 'LOSE'
    else:  # SCISSORS
        if(computerChoiceEnum == 'PAPER'):
            currentGameStatus = 'WIN'
        else:
            currentGameStatus = 'LOSE'

    if(currentGameStatus == 'WIN' or currentGameStatus == 'LOSE'):
        if(currentGameStatus == 'WIN'):
            print("You win!")
        elif(currentGameStatus == 'LOSE'):
            print("You lose!")

        playAgain = raw_input("Do you want to play again? (y/n): ")
        if(playAgain == 'Y' or playAgain == 'y'):
           currentGameStatus = 'CONTINUE'
        else:
           currentGameStatus = 'WIN'
     #if DRAW then ask again for input.