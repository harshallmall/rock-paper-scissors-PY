# Prerequisite - Import randint to generate random numbers.
from random import randint

# Step One - Player chooses either Rock, Paper, or Scissors.
player = input("Rock (Rock), Paper (Paper), Scissors (Scissors)")

# Step Two - Print result of Step One with the string "vs." to show player selection.
print(player)

# Step Three - Call random function to generate a number to simulate the computer's selection.
# Step Four - The function parameter is set to select between the integers 1, 2, or 3.
computer = randint(1, 3)

# Step Five - Create if/elif/else statement for selection to equate the integers to the strings.
# Rock == 1 && Paper == 2 && Scissors == 3
if computer == 1:
    computer = "Rock"
elif computer == 2:
    computer = "Paper"
else:
    computer = "Scissors"

# Step Six - Print result of Step One and the result of Step Five with a space instead of a new line.
print(player, "vs", computer, end=" ")