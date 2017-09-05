def level_one_board():
    level_one_board = '''
    ##############################################################
    #                 |     ___,      ___,       |               #
    #                 |      O |       O |       |               #
    #                 |     ___,      ___,       |               #
    #                 |        |       O |       |               #
    #                 |     ___,      ___,       |               #
    #                          |       O |       |               #
    #                                            |    ~~~~~~~~~~~#
    #~~~~~~~~~~~~~~~~~            ___,    __,              ___.  #
    #                |             O |      |    |          O |  #
    #                             ___,    __,    |         ___,  #
    #                                |     O|    |            |  #
    #                |            ___,    __,    |         ___,  #
    #~~   ~~~~~~~~~~~~               |      |    |          O |  #
    #                |                            ~~~~~~   ~~~~~~# 
    #                |                                 |         #
    #                |___________ _________________    |         #
    #                            |                     |         #
    ##############################################################
    '''
    return level_one_board
'''
def create_board(level_one_board):
    level_one_board = level_one_board.split("\n")
    board = []
    for elm in level_one_board:
        board.append(elm)
    
    return board
'''
def insert_player(board, width, height):
    board[height][width] = '@'
    return board
'''
def print_board(board):
    for row in board:
        print(row, end='')
'''        