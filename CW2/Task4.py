# Function used to find the total score of a given word

def getWordScore(word):
    total = 0
    # Initialises the total to be 0
    for i in word:
        try:
            total = total + getLetterScore(i)
            # Calls the letter score function for each letter in the word and adds each score together to give the final score of the word
        except TypeError:
            print("Incorrect Input")
            # Displays a message for a type error if a wrong input is given
    return total
    # Returns the total score of the word

def getLetterScore(letter):
    for i in Scores:
            if i[0] == letter:
                return i[1]
                # Finds the score of each letter using scores.txt

try:
    scoreFile = open("scores.txt")
    Scores = []
    try:
        for line in scoreFile:
            line = line.split()
            letter = line[0]
            score = int(line[1])
            Scores.append([letter,score])
    except FileNotFoundError:
        print("File Could Not Be Opened")
    except:
        print("Processing Error")
finally:
    scoreFile.close()
# Opens scores.txt into a list using the same method as task 1

input = (input("Enter a word: "))
input = input.upper()
# Asks the user to input a word and capitalises it
print(getWordScore(input))
# Calls the getWordScore function for the word and prints the return value (the score of the word)
