# Try/except statements used to read each text file into a list

try:
    scoreFile = open("scores.txt")
    Scores = []
    # Opens the text file "scores.txt" and creates a new empty list called "Scores"
    try:
        for line in scoreFile:
            line = line.split()
            letter = line[0]
            score = int(line[1])
            Scores.append([letter,score])
            # Reads each line in the text file and splits it between each space, making a nested list for each letter and corresponding score within the larger list "Scores"
    except FileNotFoundError:
        print("File Could Not Be Opened")
        # Except error displayed if the file could not be opened
    except:
        print("Processing Error")
        # Except error displayed if there was an error in processing the file
finally:
    scoreFile.close()
    # Closes the text file and ends the try/except statement

try:
    tileFile = open("tiles.txt")
    Tiles = []
    # Opens the text file "tiles.txt" and creates a new empty list called "Tiles"
    try:
        for line in tileFile:
            line = line.strip()
            Tiles.append(line)
        # Reads each line in the text file and strips away any spaces at the start and end, then appends this all into the list "Tiles"
    except FileNotFoundError:
        print("File Could Not Be Opened")
        # Except error displayed if the file could not be opened
    except:
        print("Processing Error")
        # Except error displayed if there was an error in processing the file
finally:
    tileFile.close()
    # Closes the text file and ends the try/except statement

try:
    dictionaryFile = open("dictionary.txt")
    Dictionary = []
    # Opens the text file "dictionary.txt" and creates a new empty list called "Dictionary"
    try:
        for line in dictionaryFile:
            line = line.strip()
            Dictionary.append(line)
            # Reads each line in the text file and strips away any spaces at the start and end, then appends this all into the list "Dictionary"
    except FileNotFoundError:
        print("File Could Not Be Opened")
        # Except error displayed if the file could not be opened
    except:
        print("Processing Error")
        # Except error displayed if there was an error in processing the file
finally:
    dictionaryFile.close()
    # Closes the text file and ends the try/except statement
