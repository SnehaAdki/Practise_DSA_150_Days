# Find Winner on a Tic Tac Toe Game
# https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/submissions/1832394741/

# 1275. Find Winner on a Tic Tac Toe Game
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Tic-tac-toe is played by two players A and B on a 3 x 3 grid. The rules of Tic-Tac-Toe are:

# Players take turns placing characters into empty squares ' '.
# The first player A always places 'X' characters, while the second player B always places 'O' characters.
# 'X' and 'O' characters are always placed into empty squares, never on filled ones.
# The game ends when there are three of the same (non-empty) character filling any row, column, or diagonal.
# The game also ends if all squares are non-empty.
# No more moves can be played if the game is over.
# Given a 2D integer array moves where moves[i] = [rowi, coli] indicates that the ith move will be played on grid[rowi][coli]. 
# return the winner of the game 
# if it exists (A or B). In case the game ends in a draw return "Draw". 
# If there are still movements to play return "Pending".

# You can assume that moves is valid (i.e., it follows the rules of Tic-Tac-Toe), the grid is initially empty, and A will play first.

# Example 1:
# Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
# Output: "A"
# Explanation: A wins, they always play first.

# Example 2:
# Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
# Output: "B"
# Explanation: B wins.

# Example 3:
# Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
# Output: "Draw"
# Explanation: The game ends in a draw since there are no moves to make.


def check_winner(board):
    
    # all columns
    for i in range(0,3):
        countA = 0
        countB = 0
        for j in range(0,3):
            if board[i][j] == 'X':
                countA = countA+1
            if board[i][j] == 'O':
                countB = countB+1
        if countA == 3:
            return 'A'
        elif countB == 3:
            return ' B'
    
    # all rows
    for i in range(0,3):
        countA = 0
        countB = 0
        for j in range(0,3):
            if board[j][i] == 'X':
                countA = countA+1
            if board[j][i] == 'O':
                countB = countB+1
        if countA == 3:
            return 'A'
        elif countB == 3:
            return ' B'
        
    # diagonal right-left
    if board[1][1] == board[0][0] == board[2][2] == 'X' :
        return 'A'
    elif board[1][1] == board[0][0] == board[2][2] == 'O' :
        return 'B'
    
    # diagonal left-right
    if board[2][0] == board[1][1] == board[0][2] == 'X' :
        return 'A'
    if board[2][0] == board[1][1] == board[0][2] == 'O' :
        return 'B'

    # draw & pending:
    count = 0
    for i in range(0,3):
        for j in range(0,3):
            if board[j][i] == 'X' or board[j][i] == 'O':
                count = count+1

    if count == 9:
        return 'Draw'
    return 'Pending'

def create_board(moves):
    board = [['.']*3,['.']*3,['.']*3]
    
    n = len(moves)
    for i in range(0,len(moves)):
        if i%2 ==0: #A player
            board[moves[i][0]][moves[i][1]] = 'X'
        else: #B player
            board[moves[i][0]][moves[i][1]] = 'O'
            
    print(board)
    print(check_winner(board))

moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
create_board(moves=moves)