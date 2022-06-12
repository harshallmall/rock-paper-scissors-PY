# import randint to generate random numbers
from random import randint

# players choose either from list of either rock, paper, or scissors.
options = ["Rock", "Paper", "Scissors"]

# game score variables with a global scope allow for score keeping in functions
playerScore = 0
computerScore = 0
ties = 0

# create a function to define the computerPlay's selection parameters
def computerPlay(computerOptions):
    if computerOptions == 1:
        return "Rock"
    elif computerOptions == 2:
        return "Paper"
    else:
        return "Scissors"

# call the random integer function in order to assign a number for the computerPlay
randomNumbers = randint(1, 3)

# create a function to define the playerPlay's selection parameters
def playerPlay(playerOptions, playerChoices):
    playerOptions = input("Rock, Paper, Scissors")
    playerChoices = playerOptions.lower()
    return playerOptions or playerChoices

# create function to play one round of the game and add result to score variables
def playRound(playerSelection, computerSelection):
    if playerSelection == computerSelection:
        print("Draw")
        ties += 1
    if playerSelection == "Rock" and computerSelection == "Scissors":
        print("Player wins")
        playerScore += 1
    elif playerSelection == "Rock" and computerSelection == "Paper":
        computerScore += 1
        print("Computer wins")
    elif playerSelection == "Paper" and computerSelection == "Rock":
        playerScore += 1
        print("Player wins")
    elif playerSelection == "Paper" and computerSelection == "Scissors":
        computerScore += 1
        print("Computer wins")
    elif playerSelection == "Scissors" and computerSelection == "Rock":
        playerScore += 1
        print("Player wins")
    elif playerSelection == "Scissors" and computerSelection == "Paper":
        computerScore += 1
        print("Computer wins")
    else:
        print("Draw")

# create function to play the game for five rounds with score keeping
def gamePlay():
    playerSelection = playerPlay
    computerSelection = computerPlay
    playRound(playerSelection=any, computerSelection=any)
    i = 1
    while i < 6:
        i += 1
        if playerScore == 3 or computerScore == 3:
            break
        if playerScore > computerScore:
            print("Player wins game")
        elif computerScore > playerScore:
            print("Computer wins game")

if __name__ == '__main__':
    gamePlay()