# Prerequisite - Import randint to generate random numbers.
from random import randint
# Step One - Player chooses either Rock, Paper, or Scissors.
player = input("Rock, Paper, Scissors")
# Step Two - Print result of Step One with the string "vs." to show player selection.
print(player)
# Step Three - Call random function to generate a number to simulate the computer's selection.
# The function parameter is set to select between the integers 1, 2, or 3.
computer = randint(1, 3)
# Step Four - Create if/elif/else statement for selection to equate the integers to the strings.
if computer == 1:
    computer = "Rock"
elif computer == 2:
    computer = "Paper"
else:
    computer = "Scissors"
# Step Six - Print result of Step One and the result of Step Five with a space instead of a new line.
# print(player, "vs", computer, end=" ")
# Step Seven - Compare the game results with an if/elif/else statement to determine a winner.
if player == computer:
    print("Draw")
elif player == "Rock" and computer == "Scissors":
    print("Player wins")
elif player == "Rock" and computer == "Paper":
    print("Computer wins")
elif player == "Paper" and computer == "Rock":
    print("Player wins")
elif player == "Paper" and computer == "Scissors":
    print("Computer wins")
elif player == "Scissors" and computer == "Rock":
    print("Player wins")
elif player == "Scissors" and computer == "Paper":
    print("Computer wins")
else:
    print("Draw")
# Step Eight - Print the result of the comparison of results.
print(player, "vs", computer, end=" ")