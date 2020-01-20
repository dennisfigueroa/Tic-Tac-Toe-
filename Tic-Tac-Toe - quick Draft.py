
#printing the entire board to update current state of game
def printBoard():
    print('\n')
    print(tictactoeBoard['top-left'] + '|' + tictactoeBoard['top-middle'] + '|' + tictactoeBoard['top-right'])
    print("#####")
    print(tictactoeBoard['middle-left'] + '|' + tictactoeBoard['middle-middle'] + '|' + tictactoeBoard['middle-right'])
    print("#####")
    print(tictactoeBoard['bottom-left'] + '|' + tictactoeBoard['bottom-middle'] + '|' + tictactoeBoard['bottom-right'])
def whenyouMove():
    printBoard()                    # show state of board
    print("Options are top-left, top-middle, top-right, middle-left, middle-middle, middle-right, bottom-left, bottom-middle and bottom-right")
    print("Player " + Turn + " Choose your option for where you want to move: ")
    move = input()
    if move not in list(tictactoeBoard.keys()):  #checks if the spot is a valid move based on options given
        print("That wasn't an option.")
        whenyouMove()                            #runs function again with error message if move not valid
    else:
        while True:                              # loop that checks if the spot is selected already
            if tictactoeBoard[move] == ' ':
                tictactoeBoard[move] = Turn      #if the spot is empty, then it adds the value
                break
            else:
                print("The other player has already selected this one. Try again.") #if it has been selected, runs error and begins function again
                whenyouMove()
                break

def winConditions():                            #checks if person has won
    if (Turn == listforBoard[0] == listforBoard[1] == listforBoard[2]
            or Turn == listforBoard[3] == listforBoard[4] == listforBoard[5]
            or Turn == listforBoard[6] == listforBoard[7] == listforBoard[8]
            or Turn == listforBoard[0] == listforBoard[3] == listforBoard[6]
            or Turn == listforBoard[1] == listforBoard[4] == listforBoard[7]
            or Turn == listforBoard[2] == listforBoard[5] == listforBoard[8]
            or Turn == listforBoard[0] == listforBoard[4] == listforBoard[8]
            or Turn == listforBoard[2] == listforBoard[4] == listforBoard[6]):
        return 'True'
    else:
        return 'False'

tictactoeBoard = {'top-left': ' ', 'top-middle': ' ', 'top-right': ' ', 'middle-left': ' ', 'middle-middle': ' ', 'middle-right': ' ', 'bottom-left' : ' ', 'bottom-middle': ' ', 'bottom-right' : ' '}
listforTacToeBoard = list(tictactoeBoard.values()) #creates a list of the values
while True:
    print('\n' * 100)                               #empty space for aesthetics
    print("Welcome to Tic-Tac-Toe! \nFirst player - Choose X or O: ")
    playerChoice = str(input()).upper()             #accepts even lower case
    if playerChoice in ('X', 'O'):                  #if they are correct values, then turn takes it and breaks loop
        Turn = playerChoice
        break
    else:
        print('Please Enter X or O please.')        #if not, error message
        continue
Turn = playerChoice
for i in range(9):                                  #loops and runs functions each time for maximum of 9 turns
    whenyouMove()
    listforBoard = list(tictactoeBoard.values())
    winConditions()
    if winConditions() == 'True':                   #if returned is equal to True and there is a win condition then run the congrats, if not, continue
        printBoard()
        print("Congrats Player " + Turn + "! You won!")
        break
    if Turn == 'X':
        Turn = 'O'
    else:
        Turn = 'X'
    if i == 8 and winConditions() == 'False':       #this allows the possibility of a draw 
        print("Oops! There's a Draw!")





