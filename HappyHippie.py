import startscreen
import end
import levels_board

def main():
    startscreen.print_start()
    level_one_board = levels_board.level_one_board()
    board = levels_board.create_board(level_one_board)

    player_x = 5
    player_y = 2
    
    while True:
        player_place = board[player_y][player_x]
        board = levels_board.insert_player(board, player_x, player_y)
        levels_board.print_board(board)
main()