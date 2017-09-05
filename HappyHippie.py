import startscreen
import end
import levels_board
import drawboard

def main():
    startscreen.print_start()
    level_one_board = drawboard.draw_board()
    board = drawboard.create_board(level_one_board)

    player_x = 5
    player_y = 2
    
    while True:
        player_place = board[player_y][player_x]
        board = levels_board.insert_player(board, player_x, player_y)
        drawboard.print_board(board)
main()