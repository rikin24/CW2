# Functions taken from previous tasks and simplified

def onlyEnglishLetters(word):
    for i in word:
        if i not in alphabet:
            return False
        else:
            return True

def dictionaryCheck(word):
    for i in Dictionary:
        if word in Dictionary:
            return True
        else:
            return False

def tilesCheck(word,myTiles):
    for i in word:
        if i not in myTiles or word.count(i) > myTiles.count(i):
            return False
        else:
            return True

def isValid(word,myTiles,dictionary):
    # Function used to combine the other 3 functions to check if they are all valid for the given user input
    finalCheck = False
    # Initialises finalCheck to be false
    if onlyEnglishLetters(word) == True and tilesCheck(word,myTiles) == True and dictionaryCheck(dictionary) == True:
        finalCheck = True
        # Makes finalCheck true if all 3 other functions return True
    else:
        finalCheck = False
        # finalCheck remains False if any of the other 3 functions are False
    return finalCheck
    # Returns the value of finalCheck

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

try:
    dictionaryFile = open("dictionary.txt")
    Dictionary = []
    try:
        for line in dictionaryFile:
            line = line.strip()
            Dictionary.append(line)
    except FileNotFoundError:
        print("File Could Not Be Opened")
    except:
        print("Processing Error")
finally:
    dictionaryFile.close()
# Opens dictionary.txt into a list using the same method as in task 1

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
# "alphabet" list used from task 2 to verify the word inputted only contains English letters

import random
myTiles = []
for i in range(7):
    myTiles.append(Tiles[random.randint(0,97)])
print(myTiles)
# Random function used in previous task to randomly display 7 tiles from tiles.txt in the list "myTiles"

input = (str(input("Enter a word: ")))
input = input.upper()
# Asks the user to enter a word and capitalises it
print(isValid(input,myTiles,input))
# Calls the isValid function using the user's input and myTiles, and prints the finalCheck return value
