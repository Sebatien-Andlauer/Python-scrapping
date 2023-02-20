def main():
    # asks the user for number of rows
    rows = input("Please enter the number of rows: ")   
    try :
        rows = int(rows) 
    except ValueError:
        rows = validChoice(rows)

    # asks the user for number of columns
    columns = input("Please enter the number of columns: ")    
    try :
        columns = int(columns)
    except ValueError:
        columns = validChoice(columns)
    print ("")

    # calls makeboard function and saves in board variable as list
    board = (makeBoard(rows, columns))   
    print ("Indexing starts at 0 ")
    print ("")

    # asks the user for which cells to turn on initially
    getMove = move(board, rows, columns)  
    print ("")
    while getMove != "q" :
        getMove = move(board, rows, columns)
        print ("")

    # Asks for the number of iterations to run
    iterations = input("How many iterations should I run? ")
    try:
        iterations = int(iterations) 
    except ValueError:
        iterations = validChoice(iterations)
    print ("")
    print ("Starting Board: ")
    print ("")
    printBoard(board) 
    print ("")
    iteration = 1 
    while iterations > 0 :
        print ("Iteration", iteration, ":")
        print ("")
        iteration = iteration + 1 
        board = nextIteration(board) 
        board = fixBoard(board)      
        printBoard(board) 
        print ("")
        iterations = iterations - 1 

def fixBoard(board):

    for i in range(len(board)): 
        for x in range(len(board[0])):
            if board[i][x] == 2:
                board[i][x] = 0
            if board[i][x] == 3:
                board[i][x] = 1
    return (board)

def nextIteration(board):

    rose = len(board)
    cols = len(board[0])
    for x in range(rose):
        for i in range(cols):
            counter = 0
            if (x == 0) and (i == 0):
                if (board[x][i+1] == 1) or (board[x][i+1] ==2):
                    counter = counter + 1
                if (board[x+1][i+1] == 1) or (board[x+1][i+1] ==2):
                    counter = counter + 1
                if (board[x+1][i] == 1) or (board[x+1][i] ==2):
                    counter = counter + 1
                if (board[x][i]==1):
                    if (counter == 2) or (counter == 3):
                        board[x][i] = board[x][i]
                    elif (counter < 2):
                        board[x][i] = 2
                if (board[x][i] == 0):
                    if (counter == 3):
                        board[x][i] = 3
            if (x == 0) and (0 < i < (len(board[0])-1)):
                if (board[x][i+1] == 1) or (board[x][i+1] ==2):
                    counter = counter +1
                if (board[x+1][i+1] == 1) or (board[x+1][i+1] ==2):
                    counter = counter +1
                if (board[x+1][i] == 1) or (board[x+1][i] ==2):
                    counter = counter +1
                if (board[x+1][i-1] == 1) or (board[x+1][i-1] ==2):
                    counter = counter +1
                if (board[x][i-1] == 1) or (board[x][i-1] ==2):
                    counter = counter +1
                if (board[x][i] == 1):
                    if (counter == 2) or (counter == 3):
                        board[x][i] = board[x][i]
                    elif (counter < 2):
                        board[x][i] = 2
                    elif (counter > 3):
                        board[x][i] = 2
                if (board[x][i] == 0):
                    if (counter == 3):
                        board[x][i] = 3
            if (x == 0) and (i == (len(board[0])-1)):
                if (board[x][i-1] == 1) or (board[x][i-1] ==2):
                    counter = counter + 1
                if (board[x+1][i-1] == 1) or (board[x+1][i-1] ==2):
                    counter = counter + 1
                if (board[x+1][i] == 1) or (board[x+1][i] ==2):
                    counter = counter + 1
                if (board[x][i]==1):
                    if (counter == 2) or (counter == 3):
                        board[x][i] = board[x][i]
                    elif (counter < 2):
                        board[x][i] = 2
                if (board[x][i] == 0):
                    if (counter == 3):
                        board[x][i] = 3
            if (0 < x < (len(board)-1)) and (i == 0):
                if (board[x-1][i] == 1) or (board[x-1][i] ==2):
                    counter = counter + 1
                if (board[x-1][i+1] == 1) or (board[x-1][i+1] ==2):
                    counter = counter + 1
                if (board[x][i+1] == 1) or (board[x][i+1] ==2):
                    counter = counter + 1
                if (board[x+1][i+1] == 1) or (board[x+1][i+1] ==2):
                    counter = counter + 1
                if (board[x+1][i] == 1) or (board[x+1][i] ==2):
                    counter = counter + 1
                if (board[x][i] == 1):
                    if (counter == 2) or (counter == 3):
                        board[x][i] = board[x][i]
                    elif (counter < 2):
                        board[x][i] = 2
                    elif (counter > 3):
                        board[x][i] = 2
                if (board[x][i] == 0):
                    if (counter == 3):
                        board[x][i] = 3
            if (0 < x < (len(board)-1)) and (0 < i < (len(board[0])-1)):
                if (board[x-1][i-1] == 1) or (board[x-1][i-1] ==2):
                    counter = counter +1
                if (board[x-1][i] == 1) or (board[x-1][i] ==2):
                    counter = counter +1
                if (board[x-1][i+1] == 1) or (board[x-1][i+1] ==2):
                    counter = counter +1
                if (board[x][i+1] == 1) or (board[x][i+1] ==2):
                    counter = counter +1
                if (board[x+1][i+1] == 1) or (board[x+1][i+1] ==2):
                    counter = counter +1
                if (board[x+1][i] == 1) or (board[x+1][i] ==2):
                    counter = counter +1
                if (board[x+1][i-1] == 1) or (board[x+1][i-1] ==2):
                    counter = counter +1
                if (board[x][i-1] == 1) or (board[x][i-1] ==2):
                    counter = counter +1
                if (board[x][i] == 1):
                    if (counter == 2) or (counter == 3):
                        board[x][i] = board[x][i]
                    elif (counter < 2):
                        board[x][i] = 2
                    elif (counter > 3):
                        board[x][i] = 2
                if (board[x][i] == 0):
                    if (counter == 3):
                        board[x][i] = 3
            if (0 < x < (len(board)-1)) and (i == (len(board[0])-1)):
                if (board[x-1][i] == 1) or (board[x-1][i] ==2):
                    counter = counter + 1
                if (board[x-1][i-1] == 1) or (board[x-1][i-1] ==2):
                    counter = counter + 1
                if (board[x][i-1] == 1) or (board[x][i-1] ==2):
                    counter = counter + 1
                if (board[x+1][i-1] == 1) or (board[x+1][i-1] ==2):
                    counter = counter + 1
                if (board[x+1][i] == 1) or (board[x+1][i] ==2):
                    counter = counter + 1
                if (board[x][i] == 1):
                    if (counter == 2) or (counter == 3):
                        board[x][i] = board[x][i]
                    elif (counter < 2):
                        board[x][i] = 2
                    elif (counter > 3):
                        board[x][i] = 2
                if (board[x][i] == 0):
                    if (counter == 3):
                        board[x][i] = 3
            if (x == (len(board)-1)) and (i == 0):
                if (board[x-1][i] == 1) or (board[x-1][i] ==2):
                    counter = counter + 1
                if (board[x-1][i+1] == 1) or (board[x-1][i+1] ==2):
                    counter = counter + 1
                if (board[x][i+1] == 1) or (board[x][i+1] ==2):
                    counter = counter + 1
                if (board[x][i]==1):
                    if (counter == 2) or (counter == 3):
                        board[x][i] = board[x][i]
                    elif (counter < 2):
                        board[x][i] = 2
                if (board[x][i] == 0):
                    if (counter == 3):
                        board[x][i] = 3
            if ( x == (len(board)-1)) and ( i == (len(board[0])-1)):
                if (board[x-1][i] == 1) or (board[x-1][i] ==2):
                    counter = counter + 1
                if (board[x-1][i-1] == 1) or (board[x-1][i-1] ==2):
                    counter = counter + 1
                if (board[x][i-1] == 1) or (board[x][i-1] ==2):
                    counter = counter + 1
                if (board[x][i]==1):
                    if (counter == 2) or (counter == 3):
                        board[x][i] = board[x][i]
                    elif (counter < 2):
                        board[x][i] = 2
                if (board[x][i] == 0):
                    if (counter == 3):
                        board[x][i] = 3
            if (x == (len(board)-1)) and (0 < i < (len(board[0])-1)):
                if (board[x][i-1] == 1) or (board[x][i-1] ==2):
                    counter = counter + 1
                if (board[x-1][i-1] == 1) or (board[x-1][i-1] ==2):
                    counter = counter + 1
                if (board[x-1][i] == 1) or (board[x-1][i] ==2):
                    counter = counter + 1
                if (board[x-1][i+1] == 1) or (board[x-1][i+1] ==2):
                    counter = counter + 1
                if (board[x][i+1] == 1) or (board[x][i+1] ==2):
                    counter = counter + 1
                if (board[x][i] == 1):
                    if (counter == 2) or (counter == 3):
                        board[x][i] = board[x][i]
                    elif (counter < 2):
                        board[x][i] = 2
                    elif (counter > 3):
                        board[x][i] = 2
                if (board[x][i] == 0):
                    if (counter == 3):
                        board[x][i] = 3
    return (board)

def move(board, rows, columns):

    row = input("Please enter the row of a cell to turn on or q to exit: ")
    if row == "q" :
        return ("q")  
    else:
        try :
            row = int(row)
        except ValueError:
            row = validChoice(row)
        while row >= rows :
            row = validChoice(row)
    col = input("Please enter a column for that cell: ")
    try :
        col = int(col)
    except ValueError:
        col = validChoice(col)
    while col >= columns:
        col = validChoice(col)
    board[row][col] = 1
    return (board)


def printBoard(board):

    for i in range(len(board)):
        for x in range(len(board[0])):
            if (board[i][x]) == 0:
                print (0, end="")
            elif (board[i][x]) == 1:
                print ('X', end="")
        print ("")
  
def makeBoard(rows, columns):

    list2 = []  
    column = columns
    while rows > 0:
        list1 = [] 
        while column > 0:
            list1.append(0)
            column = column - 1
        list2.append(list1)
        rows = rows - 1
        column = columns
    return (list2)

def validChoice(number):

    number = input("Please enter a valid choice: ")
    try :
        number = int(number)
    except ValueError:
        number = validChoice(number)
    return (number)

main()