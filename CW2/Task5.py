# Function used to check if the inputted word can be made out of the random set of tiles given

def tilesCheck(word,myTiles):
    check = False
    # Initialises check to be False
    for i in word:
        if i not in myTiles or word.count(i) > myTiles.count(i):
            check = False
            # Cycles through each letter of the word and if the letter is not found in myTiles or is used more times than there are in myTiles then check is made false
        else:
            check = True
            # As long as each letter of the word can be used from myTiles, check remains True
    if check == True:
        result = "Word is valid"
        # If check remains True by the end of the for loop, the message above is displayed
    elif check == False:
        result = "Word is invalid"
        # If check remains False by the end of the for loop, the message above is displayed
    return result
    # Returns the message corresponding to the value of check

try:
    tileFile = open("tiles.txt")
    Tiles = []
    try:
        for line in tileFile:
            line = line.strip()
            Tiles.append(line)
    except FileNotFoundError:
        print("File Could Not Be Opened")
    except:
        print("Processing Error")
finally:
    tileFile.close()
# Opens tiles.txt into a list using the same method as in task 1

import random
myTiles = []
for i in range(7):
    myTiles.append(Tiles[random.randint(0,97)])
print(myTiles)
# Uses a random integer function to randomly display 7 tiles from tiles.txt in a list

input = (input("Enter a word: "))
input = input.upper()
# Asks the user to input a word and capitalises it
print(tilesCheck(input,myTiles))
# Calls the tilesCheck function using the user's word and the randomly generated myTiles and prints the return value
