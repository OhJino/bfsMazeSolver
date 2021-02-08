from array import *

def movement(curr_row, curr_column, move_row, move_column, game_set, trail):
    print(move_row)
    print(move_column)
    if((move_row > 6) or (move_column > 6)):
        if((move_row < 0) or (move_column < 0)):
            print("hi")
            return game_set
    else:
        print("ho")
        game_set[move_row][move_column] = 'O'
        game_set[curr_row][curr_column] = trail
        for item in game_set:
            print(item)
        return game_set

def moveBack(cu_row, cu_column, maze_set):
    back_up = False
    back_down = False
    back_left = False
    back_right = False
    if (maze_board[cu_row - 1][cu_column] == '-'):
        back_up = True
        cu_row -= 1
        f_spot = "DOWN"
        return back_up, back_down, back_left, back_right, cu_row, cu_column, f_spot
    elif (maze_board[cu_row][cu_column + 1] == '-'):
        back_right = True
        cu_column += 1
        f_spot = "LEFT"
        return back_up, back_down, back_left, back_right, cu_row, cu_column, f_spot
    elif (maze_board[cu_row][cu_column - 1] == '-'):
        back_left = True
        cu_column -= 1
        f_spot = "RIGHT"
        return back_up, back_down, back_left, back_right, cu_row, cu_column, f_spot
    elif (maze_board[cu_row+ 1][cu_column] == '-'):
        back_down = True
        cu_row += 1
        f_spot = "UP"
    return back_up, back_down, back_left, back_right, cu_row, cu_column, f_spot


def planNextMove(c_row, c_column, game_board, false_point):
    move_up = False
    move_right = False
    move_left = False
    move_down = False
    falser_spot = ""
    print("Checking next move")
    if (maze_board[c_row - 1][c_column] == ' '):
        if(false_point != "UP"):
            move_up = True
            falser_spot = "DOWN"
    if (maze_board[c_row][c_column + 1] == ' '):
        if(false_point != "RIGHT"):
            move_right = True
            falser_spot = "LEFT"
    if (maze_board[c_row][c_column - 1] == ' '):
        if(false_point != "LEFT"):
            move_left = True
            falser_spot = "RIGHT"
    try:
        if (maze_board[c_row+ 1][c_column] == ' '):
            if(false_point != "DOWN"):
                move_down = True
                falser_spot = "UP"
    except:
        pass
    return move_up, move_down, move_left, move_right, falser_spot

def move(m_up, m_right, m_left, m_down, prev_row, prev_column, f_spot, game):
        game_set = movement(previous_row, previous_column, (previous_row - 1), previous_column, maze, '-')
        print("Moved up")
        m_up, m_down, m_left, m_right, f_spot = planNextMove((prev_row - 1), prev_column, game, f_spot)
        previous_row -= #MAKE THIS A PARRAMETER
        m_down = False # MAKE THIS A PARAMETER


def movePiece(mv_up, mv_right, mv_left, mv_down, current_row, current_column, win_spot, maze, false_spot):
    print(false_spot)
    previous_row = current_row
    previous_column = current_column
    if(maze[0][win_spot] == 'O'):
        print("Winner!")
        print(win_spot)
        return
    if(mv_up):
        game_set = movement(previous_row, previous_column, (previous_row - 1), previous_column, maze, '-')
        print("Moved up")
        mv_up, mv_down, mv_left, mv_right, false_spot = planNextMove((previous_row - 1), previous_column, maze, false_spot)
        previous_row -= 1
        mv_down = False
        movePiece(mv_up, mv_right, mv_left, mv_down, previous_row, previous_column, win_spot, maze, false_spot)
    elif(mv_right):
        game_set = movement(previous_row, previous_column, previous_row, (previous_column + 1), maze, '-')
        print("Moved right")
        mv_up, mv_down, mv_left, mv_right, false_spot = planNextMove(previous_row, (previous_column + 1), maze, false_spot)
        previous_column +=1
        mv_left = False
        movePiece(mv_up, mv_right, mv_left, mv_down, previous_row, previous_column, win_spot, maze, false_spot)
    elif(mv_left):
        game_set = movement(previous_row, previous_column, previous_row, (previous_column - 1), maze, '-')
        print("Can't move right")
        mv_up, mv_down, mv_left, mv_right, false_spot = planNextMove(previous_row , (previous_column - 1), maze, false_spot)
        previous_column -= 1
        mv_right = False
        movePiece(mv_up, mv_right, mv_left, mv_down, previous_row, previous_column, win_spot, maze, false_spot)
    elif(mv_down):
        game_set = movement(previous_row, previous_column, (previous_row + 1), previous_column, maze, '-')
        print("Can't move up")
        mv_up, mv_down, mv_left, mv_right, false_spot = planNextMove(previous_row, (previous_column + 1), maze, false_spot)
        previous_row += 1
        mv_up = False
        movePiece(mv_up, mv_right, mv_left, mv_down, previous_row, previous_column, win_spot, maze, false_spot)
    else:
        print("moving back")
        new_row = 0
        new_column = 0
        mv_up, mv_down, mv_left, mv_right, new_row, new_column, false_spot = moveBack(previous_row, previous_column, maze)
        game_set = movement(previous_row, previous_column, new_row, new_column, maze, ' ')
        mv_up, mv_down, mv_left, mv_right, false_spot = planNextMove(new_row, new_column, maze, false_spot)
        movePiece(mv_up, mv_right, mv_left, mv_down, new_row, new_column, win_spot, maze, false_spot)


maze_board = []
maze_board.append(['X', 'X', 'X', ' ', 'X', 'X'])
maze_board.append(['X', ' ', 'X', ' ', ' ', 'X'])
maze_board.append(['X', ' ', ' ', 'X', ' ', 'X'])
maze_board.append(['X', 'X', ' ', 'X', ' ', 'X'])
maze_board.append(['X', 'X', ' ', ' ', ' ', 'X'])
maze_board.append(['X', ' ', ' ', 'X', 'X', 'X'])
maze_board.append(['O', ' ', 'X', 'X', 'X', 'X'])
maze_board = []

for row in maze_board:
    try:
        piece_row_index = maze_board.index(row)
        piece_column_index = row.index('O')
        break
    except:
        pass

#print(maze_board[0].index(' '))

up = False
right = False
left = False
down = False
fake_spot = "DOWN"
winner_spot = maze_board[0].index(' ')
up, down, left, right, fake_spot = planNextMove(piece_row_index, piece_column_index, maze_board, fake_spot)
movePiece(up, right, left, down, piece_row_index, piece_column_index, winner_spot, maze_board, fake_spot)

#End Maze Display
for row in maze_board:
    print(row)