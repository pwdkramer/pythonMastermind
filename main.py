#Patrick Kramer
#CodeCademy portfolio project 1: Mastermind
#1/4/22

print("Welcome to Mastermind!")

#select difficulty
print("Please select a difficulty: (n/h)")
user_difficulty = input()
while user_difficulty.lower() != "n" and user_difficulty.lower() != "h":
  print("Please enter either 'n' or 'h'")
  user_difficulty = input()
