from board import Board

gridsize = 10

board = Board(10,25)

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