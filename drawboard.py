import levels_board

def draw_board():
    level_one_board = levels_board.level_one_board()
    return level_one_board

def create_board(level_one_board):
    level_one_board = level_one_board.split("\n")
    board = []

    for element in level_one_board:
        board.append(list(element))
    return board
    
def print_board(board):
    for row in board:
        for char in row:
            print(char, end='')
        print()

def insert_player(board, width, height):
    board[height][width] = '@'
    return board