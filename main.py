from board import Board

# Square board side length
gridsize = 10
# Number of mines in game
mines = 25

board = Board(gridSize, mines)

while True:
    board.displayBoard()
    choice = input("Enter coordinates like so x,y or enter F to go into flagging mode: ")
    if choice.lower() == "f":
        newChoice = input("Enter coordinates to flag/unflag as x,y: ")
        board.flagUnflag(int(str(newChoice)[0]), int(str(newChoice)[2]))
    elif len(choice) == 3:
        check = board.pickSpot(int(str(choice)[0]), int(str(choice)[2]))
        if check == -1:
            print("You hit a mine!")
            break
