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

#compare userGuess with secret code and provide feedback
def compareCode(secret_code, user_guess):
    game_won = False
    perfect_pins = 0
    wrong_position = 0
    if secret_code == user_guess: #correct guess, user wins
        game_won = True
        perfect_pins = 4
    else: #provide feedback on guess
        temp_code = []
        temp_guess = []
        for i in range(len(user_guess)): #check for perfect pins
            if user_guess[i] == secret_code[i]:
                perfect_pins += 1
            else:
                temp_code.append(secret_code[i])
                temp_guess.append(user_guess[i])
        for i in range(len(temp_guess)): #check for right color wrong position
            for j in range(len(temp_code)):
                if temp_guess[i] == temp_code[j]:
                    wrong_position += 1
                    temp_code[j] = "0"
                    break

    print("Correct color correct position: {}".format(perfect_pins))
    print("Correct color wrong position: {}".format(wrong_position))

    return game_won

#game loop with turn counter
def playGame(diff, secret_code):
    turn_count = 1
    game_won = False
    while turn_count <= 10 and game_won == False:
        print("---------------------------------")
        print("Turn {}:".format(turn_count))
        user_guess = getGuess(diff)
        game_won = compareCode(secret_code, user_guess)
        turn_count += 1
    print("---------------------------------")
    if game_won == True:
        print("Congratulations! You win!")
    else:
        print("Game over...")
    print("The secret code was: {}".format(secret_code))

#main game
print("Welcome to Mastermind!")
diff = chooseDifficulty()
secret_code = makeCode(diff)
playGame(diff, secret_code)