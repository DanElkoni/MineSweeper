from Board import Board

gridsize = int(input("Enter a sidelength for the square minesweeper grid: "))
mines = int(input(f"How many mines would you like on the board? (Reccomended {(gridsize**2)/4})"))

board = Board(gridsize,mines)

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
