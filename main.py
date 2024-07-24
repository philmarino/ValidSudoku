def isValidSudoku(board):
    #horizontals
    for index in range(9):
        row = board[index]
        if not unique(row):
            return False
        
        column = [board[0][index],board[1][index],board[2][index],board[3][index],board[4][index],board[5][index],board[6][index],board[7][index],board[8][index]]
        if not unique(column):
            return False

    for h in range(0,6,3):
        for v in range(0,6,3):
            square = [board[v][h],board[v][h+1],board[v][h+2],board[v+1][h],board[v+1][h+1],board[v+1][h+2],board[v+2][h],board[v+2][h+1],board[v+2][h+2]]
            if not unique(square):
                return False

    return True

def unique(sample):
    trimed = ''
    for square in sample:
        if square == '.':
            pass
        else:
            trimed += square
    
    if len(trimed) == len(set(trimed)):
        return True
    return False

#Example 1:
#Input: 
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(board))
#Output: true

#Example 2:
#Input: 
board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(board))
#Output: false
#Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

