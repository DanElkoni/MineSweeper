import random
import numpy as np

# Global constants
MINE = -1
FLAGGED = 2
HIDDEN = 0
DISPLAYED = 1

class Board:
    def __init__(self, gridSize, numMines):
        self.board = [[HIDDEN for _ in range(gridSize)] for _ in range(gridSize)]
        self.display = [[HIDDEN for _ in range(gridSize)] for _ in range(gridSize)]
        self.numMines = numMines
        self.flagCount = 0

        self.gridSize = gridSize

        # Generating mines randomly
        self.placeMines(0, numMines, gridSize)

        self.displayDebug()

        # Assigning mine count values to each grid square
        circleArr = [[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1]]
        for row in range(0,gridSize):
            for col in range(0,gridSize):
                currArr = [[row,col]]*8
                currArr = np.add(currArr,circleArr)
                num = 0
                counted = []
                if self.board[row][col] != MINE:
                    for i in range(0,8):
                        newRow = currArr[i][0]
                        newCol = currArr[i][1]
                        if 0 <= newRow < gridSize and 0 <= newCol < gridSize:
                            if self.board[row][col] != -1:
                                if self.board[newRow][newCol] == -1:
                                    if [newRow,newCol] not in counted:
                                        counted.append([newRow,newCol])
                                        num += 1
                    self.board[row][col] = num
                
    def placeMines(self, currMines, totalMines, gridSize):
        if currMines == totalMines:
            return
        else:
            row = random.randint(0, gridSize - 1)
            col = random.randint(0, gridSize - 1)

            if self.board[row][col] != MINE:
                self.board[row][col] = MINE
                currMines += 1  # only increment if you actually placed a mine

            self.placeMines(currMines, totalMines, gridSize)

    # Basic Getters
    def getSize(self):
        return self.gridSize
    
    def getDisp(self):
        return self.display
    
    # Flag/Unflag function
    def flagUnflag(self, col, row):
        col-=1
        row-=1
        if self.display[row][col] == FLAGGED:
            self.display[row][col] = HIDDEN
            self.flagCount -= 1
        elif self.display[row][col] == HIDDEN:
            self.display[row][col] = FLAGGED
            self.flagCount += 1
    
    # Picking a spot functionality
    def pickSpot(self, col, row):
        col-=1
        row-=1
        if self.board[row][col] == -1:
            return -1
        else:
            self.display[row][col] = DISPLAYED

    def displayBoard(self):
        # Displaying top row of indexes
        print("\n", end="")
        print("      ", end="")
        for p in range(0, self.gridSize):
            print(p+1, end="")
            for g in range(0, 3-len(str(p+1))):
                print(" ", end="")
        print("\n",end="")
        
        # Main Board Display
        for row in range(0, self.gridSize):
            print(f"\n{row+1}", end="")
            for i in range(0,6-len(str(row+1))):
                print(" ", end="")
            for col in range(0, self.gridSize):
                if self.display[row][col] == HIDDEN:
                    print("X  ", end="")
                elif self.display[row][col] == DISPLAYED:
                    print(f"{self.board[row][col]}  ",end="")
                elif self.display[row][col] == FLAGGED:
                    print("F  ",end="")
        print("\n")
        print(f"Mines left: {self.numMines-self.flagCount}\n")

    def displayDebug(self):
        # Displaying top row of indexes
        print("\n", end="")
        print("      ", end="")
        for p in range(0, self.gridSize):
            print(p+1, end="")
            for g in range(0, 3-len(str(p+1))):
                print(" ", end="")
        print("\n",end="")
        
        # Main Board Display
        for row in range(0, self.gridSize):
            print(f"\n{row+1}", end="")
            for i in range(0,6-len(str(row+1))):
                print(" ", end="")
            for col in range(0, self.gridSize):
                if self.board[row][col] == MINE:
                    print("M  ", end="")
                else:
                    print(f"{self.board[row][col]}  ", end="")
        print("\n")