# Function used to find the corresponding score given to a certain letter used from the alphabet

def getLetterScore(letter):
    for i in Scores:
        try:
            if i[0] == letter:
                return i[1]
            # Finds the line of the score file for the inputted letter and gives the corresponding score for it
        except TypeError:
            print("Incorrect Input")
            # Returns a message for a type error if a wrong input is given, e.g. "2"
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
# scores.txt file opened into a list in same method as task 1

input = (input("Enter a letter: "))
input = input.upper()
# Asks the user to input a letter and makes it capitalised
print(getLetterScore(input))
# Calls the getLetterScore function and prints the return value (the corresponding score)
