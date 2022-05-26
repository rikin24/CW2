# Function used to check if the inputted word only contains English letters

def onlyEnglishLetters(word):
    # Defines the function
    check = False
    # Originally assigns check to be False
    for i in word:
        if i not in alphabet:
            check = False
            break
            # Checks each character in the word and if it's not in the list "alphabet" then check is made false and the loop is stopped
        else:
            check = True
            # As long as each character in the word is in "alphabet", check remains True
    if check == True:
        eng = "The word only contains English letters (True)"
        # If check remains true at the end of the for loop then the message above is returned
    else:
        eng = "The word does not only contain English Letters (False)"
        # If check remains false at the end of the for loop then the message above is returned
    return eng

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
# Creates a new list called "alphabet" that contains each letter of the alphabet
input = (str(input("Enter a word: ")))
# Asks the user to input a word
print(onlyEnglishLetters(input))
# Calls the onlyEnglishLetters function and prints the return value
