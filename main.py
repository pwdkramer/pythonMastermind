#Patrick Kramer
#CodeCademy portfolio project 1: Mastermind
#1/4/22

from random import randrange

def chooseDifficulty():
    print("Please select a difficulty: (n/h)")
    user_difficulty = input()
    while user_difficulty.lower() != "n" and user_difficulty.lower() != "h":
        print("Please enter either 'n' or 'h'")
        user_difficulty = input()
    return user_difficulty.lower()


#possible colors on nomral: Red, Yellow, Green, blUe
#added colors on hard: Black, White
def makeCode(diff):
    secret_code = ""
    for i in range(4):
        if diff == "n":
            roll = randrange(1, 5)
        elif diff == "h":
            roll = randrange(1,7)
        else:
            print("Difficulty error in makeCode()")
        #print(roll)
        if roll == 1:
            secret_code += "R"
        elif roll == 2:
            secret_code += "Y"
        elif roll == 3:
            secret_code += "G"
        elif roll == 4:
            secret_code += "U"
        elif roll == 5:
            secret_code += "B"
        elif roll == 6:
            secret_code += "W"
        else:
            print("Error with range of roll in makeCode()")
    return secret_code

#get guess from user
def getGuess(diff):
    valid_colors = "RYGU"
    print("Please enter your guess of four colors.")
    if diff == "n":
        print("The colors to choose from are: R, Y, G, U")
    elif diff == "h":
        valid_colors += "BW"
        print("The colors to choose from are R, Y, G, B, B, W")
    else:
        print("Error with diff in getGuess()")
    
    print("Please enter your guess:")
    user_guess = input().upper()
    valid_guess = True
    if len(user_guess) != 4:
        valid_guess = False
    for i in range(len(user_guess)):
        if user_guess[i] not in valid_colors:
            valid_guess = False
    while valid_guess == False:
        print("Illegal guess: Please enter 4 letters from the list of possible colors:")
        user_guess = input().upper()
        valid_guess = True
        if len(user_guess) != 4:
            valid_guess = False
        for i in range(len(user_guess)):
            if user_guess[i] not in valid_colors:
                valid_guess = False
    return user_guess


print("Welcome to Mastermind!")

#select difficulty
diff = chooseDifficulty()
secret_code = makeCode(diff)
user_guess = getGuess(diff)

print(secret_code)