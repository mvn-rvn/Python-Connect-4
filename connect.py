#initialize the 2d array
grid = []
while len(grid) != 7:
    grid.append(["-", "-", "-", "-", "-", "-", "-"])

#initialize turn order

#REMINDER: grid[y][x]. y coordinate goes from top to bottom
def printgrid():
    print("\n0 1 2 3 4 5 6")
    for row in grid:
        for elem in row:
            print(elem + " ", end="")
        print(" ")
    print("----------------------------------------------")

#check for wins (disgusting code)
def checkforwin():
    #vertical wins
    for y in range(len(grid) - 3):
        for x in range(len(grid[0])):
            piece = grid[y][x]
            if piece != "-":
                if grid[y][x] == piece and grid[y+1][x] == piece and grid[y+2][x] == piece and grid[y+3][x] == piece:
                    return True
        #horizontal wins
    for y in range(len(grid)):
        for x in range(len(grid[0]) - 3):
            piece = grid[y][x]
            if piece != "-":
                if grid[y][x] == piece and grid[y][x+1] == piece and grid[y][x+2] == piece and grid[y][x+3] == piece:
                    return True
    #diagonal down wins
    for y in range(len(grid) - 3):
        for x in range(len(grid[0]) - 3):
            piece = grid[y][x]
            if piece != "-":
                if grid[y][x] == piece and grid[y+1][x+1] == piece and grid[y+2][x+2] == piece and grid[y+3][x+3] == piece:
                    return True
    #diagonal up wins
    for y in range(len(grid) - 4, len(grid)):
        for x in range(len(grid[0]) - 3):
            piece = grid[y][x]
            if piece != "-":
                if grid[y][x] == piece and grid[y-1][x+1] == piece and grid[y-2][x+2] == piece and grid[y-3][x+3] == piece:
                    return True

#main loop
def gameloop():
    turn = "X"
    while True:
        #get input
        printgrid()
        action = int(input(turn + "'s turn. "))
        #place piece
        bottom = False
        row = 0
        while bottom == False:
            if grid[0][action] == "-" and (row + 1 == len(grid) or grid[row + 1][action] != "-"):
                grid[row][action] = turn
                bottom = True
            elif grid[0][action] != "-":
                print("Bruh that column's full")
                bottom = True
            row += 1
        #check for winners
        if checkforwin() == True:
            printgrid()
            print("WINNER: " + turn)
            break
        #advance turn order
        if turn == "X":
            turn = "O"
        else:
            turn = "X"

gameloop()