#########################
# CMPT 120 - Final Project: Colourful Zero Game
# ########## & Gia Hue Mai
# Aug 1, 2022
# main.py file
import cmpt120image
import myCreateImages

def initialBoard(boardNum):
    boardList = []
    board = "board" + boardNum + ".csv"
    boardFile = open(board)
    firstLine = boardFile.readline()
    # Reading csv
    for line in boardFile:
        lineList = line.strip().split(",")
        
        # convert string to int in the list before adding it to the boardList
        for x in range(len(lineList)):
            lineList[x] = int(lineList[x])

        # Add list into the big list
        boardList.append(lineList)  
    return boardList

def printBoard(boardList, sumColList, sumRowList):
    # Creating Column # list
    columnListTitle = []
    boardSize = (len(boardList))
    for value in range(boardSize):
        colValue = "Col " + str(value)
        columnListTitle.append(colValue)   
    columnListTitle.append("Sum")

    # empty strings to do .format later based on boardsize
    rowEmptyFormat = "{:>7} "*(boardSize + 1)
    colSumEmptyFormat = "{:>7} "*(boardSize)
    # Print out the board
    print ("     ", rowEmptyFormat.format(*columnListTitle))
    for row in range(boardSize):
        print("\nRow", row, rowEmptyFormat.format(*boardList[row], sumRowList[row]))
    print ("\n  Sum", colSumEmptyFormat.format(*sumColList))

# Calculates the sum of each row 
def calcSumRow(boardList):
    sumRowList = []
    for x in range(len(boardList)):
        sum = 0
        for num in boardList[x]:
            sum = sum+num
        sumRowList.append(sum)
    return sumRowList

# Calculates the sum of each column
def calcSumCol(boardList):
    sumColList = []
    for x in range(len(boardList)):
        sum = 0
        for num in range(len(boardList)):
            column = boardList[num][x]
            sum = sum+column
        sumColList.append(sum)
    return sumColList

# checks for integer in the user input
def validDigit(input, boundaryList):
    if input in boundaryList:
        boolValue = False
        input = int(input)
    else:
        print ("That is not a valid value, please re-enter")
        boolValue = True
    return input, boolValue
    
def isZero(sumList):
    point = 0
    for y in range(len(sumList)):
        if sumList[y] == 0:
            point += 1
    return point

# Absolute value so that it does false detect a win
def sumOfList(sumList):
    sum = 0
    for num in sumList:
        sum = sum + abs(num)
    return sum          

# The main code
optionInput = ["1", "2", "3", "4", "5"]
validValues9 = ["-9", "-8", "-7", "-6", "-5", "-4", "-3", "-2", "-1", 
                "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# Variables
pointTotal = 0
userGame = True
userFirstInput = True
gameNumber = 0
gamesWon = 0

# Colorcoding.csv file dictionary
colourDict = myCreateImages.colourDictCreation()

print("""Dear player! Welcome to the "Coulourful Zero" game
==================================================

With this system you will be able to play as many games as you want!

The objective of this game is to make all board rows and columns sum to 0

For each game: 
- you will be able to choose an initial board,
- at the end of each game you will win points, and
- you will see an image representation of the last board.
Enjoy! \n""")


# Asks if user wants to play (FIRST interaction)
while userFirstInput:
    userPlay = input("Would you like to play? (y/n): ")
    if userPlay == 'y':
        userFirstInput = False
    elif userPlay == "n":
        userGame = False
        print ("Have a great day!")
        userFirstInput = False
    else:
        print ("Input is invalid, please enter 'y' or 'n'")

# The game (everything will happen in here)
while userGame:
    if userPlay == 'y':
        point = 0
        gameNumber += 1
        print ("\nGame number: {} \n===============\n".format(gameNumber))
    
        pickBoard = True
        # Asks user to choose a board and get them out of loop when answered
        while pickBoard:
            boardNumInput = input("Which initial board do you want to use (1, 2, 3, 4 or 5): ")
            if boardNumInput in optionInput:
                pickBoard = False
            else:
                print ("Unknown input, please enter a valid value.\n")
                
        # Read csv file
        boardList = initialBoard(boardNumInput)
        
        # Calculate turns
        boardSize = len(boardList)
        turns = boardSize**2//2
        
        # for user input checking later on (for row,col,val)
        listCheck = ['99']
        for c in range(boardSize):
            listCheck += str(c)
        
        # Print initial board
        sumRowList = calcSumRow(boardList)
        sumColList = calcSumCol(boardList)

        print ("\nThe board is \n---------------\n"
               "\n(initial board) \n") 
        printBoard(boardList, sumColList, sumRowList)
        print ("\nTurns left:", turns)

        while turns > 0:
            rowInput = True
            colInput = True
            valInput = True
            
            # Row input
            print("\nUser, where do you want your value?"
                  " (row 99 if you want no more turns)")
            while rowInput:
                userRow = input("Row? (>= 0 and <= {}): ".format(boardSize-1))
                userRow, rowInput = validDigit(userRow, listCheck)    
            if userRow == 99:
                turns = 0
                
            # if user does not input 99
            else:
                while colInput:
                    userCol = input("Col? (>= 0 and <= {}): ".format(boardSize-1))
                    userCol, colInput = validDigit(userCol, listCheck)
      
                while valInput:
                    userVal = input("Value? (>= -9 and <= 9): ")
                    userVal, valInput = validDigit(userVal, validValues9)         

                boardList [userRow][userCol] = userVal

                turns = turns-1
            
                # Sum Calculation
                sumRowList = calcSumRow(boardList)
                sumColList = calcSumCol(boardList)

                # Print out the board
                print ("\nThe board is\n-------------\n")
                printBoard(boardList, sumColList, sumRowList)
 
                sumAllZero = sumOfList(sumRowList) + sumOfList(sumColList)
                if sumAllZero == 0:
                    turns = 0
                # Only prints when turns is not 0
                if turns != 0:
                    print ("\nTurns left:", turns)
        # End of Game
        # Tally points
        point += isZero(sumRowList)
        point += isZero(sumColList)
            
        # Check if user won the game
        if point == len(sumRowList)*2:
            point += 10
            gamesWon += 1
            print ("\nYey! the game is over because you won!\n" 
                    "\nYey! Congratulations again, user, you won this game!\n"
                    "You got {} points".format(point))
        else:
            if userRow == 99:
                print ("Since you didn't want to update more digits, the game is over")
            else:
                print("\nYou reached the maximum turns possible, the game is over!")
            print("\nSo sorry, User, you lost this game!")
            if point == 0:
                print("And no points either... next time!")
            else:
                print("You still got points!: {}".format(point))
        # Add to the total for all games
        pointTotal += point
        
        # create board image
        print("\nAnd now, check the image based on the last board state!!")
        # board number for saving image
        boardNumber = int(boardNumInput)

        imageBoard = cmpt120image.getBlackImage(100*boardSize, 100*boardSize)
        for x in range(boardSize):
            for y in range(boardSize):
                number = boardList[x][y] 
                colour = myCreateImages.rgbInvert(number, colourDict)
                imageBoard = myCreateImages.fillSquare(x, y, imageBoard, colour)
        cmpt120image.saveImage(imageBoard, "boardimage{}-{}.jpg".format(boardNumber, gameNumber))
        
        # diagonal image
        imageBoard = cmpt120image.getBlackImage(100, 100*boardSize)
        for j in range(boardSize):
            number = boardList[j][j]
            colour = myCreateImages.rgbInvert(number, colourDict)
            imageBoard = myCreateImages.fillSquare(j, 0, imageBoard, colour)
        cmpt120image.saveImage(imageBoard, "diagimage{}-{}.jpg".format(boardNumber, gameNumber))

        # Once finished, asks they want to play again
        userPlay = input ("\nWould you like to play another game? (y/n): ")

    elif userPlay == "n":
        userGame = False
        print ("\nTOTALS ALL GAMES \n"
                "Total points user in all games: {} \n"
                "Total games the user won: {}".format(pointTotal, gamesWon))
        print ("\nBye!")

    else:
        print ("Input is invalid, please enter 'y' or 'n'\n")
        userPlay = input ("Would you like to play another game? (y/n): ")