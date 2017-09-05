import startscreen
import end
import levels_board
import drawboard
import getch
import os


def main():
    #startscreen.print_start()
    level_one_board = drawboard.draw_board()
    board = drawboard.create_board(level_one_board)

    player_x = 5
    player_y = 2
    
    while True:
        player_place = board[player_y][player_x]
        board = drawboard.insert_player(board, player_x, player_y)
        drawboard.print_board(board)
        key = getch.getch()
        os.system("clear")

        if key == 'w':
            player_y -= 1
            if board[player_y][player_x] == '#' or board[player_y][player_x] == '|' or  board[player_y][player_x] == '~' or board[player_y][player_x] == '_' or board[player_y][player_x] == ',' :
                player_y += 1

        elif key == 'a':
            player_x -= 1
            if board[player_y][player_x] == '#' or board[player_y][player_x] == '|' or  board[player_y][player_x] == '~'  or  board[player_y][player_x] == '~' or board[player_y][player_x] == '_' or board[player_y][player_x] == ',':
                player_x += 1

        elif key == 's':
            player_y += 1
            if board[player_y][player_x] == '#' or board[player_y][player_x] == '|' or  board[player_y][player_x] == '~'  or  board[player_y][player_x] == '~' or board[player_y][player_x] == '_' or board[player_y][player_x] == ',':
                player_y -= 1

        elif key == 'd':
            player_x += 1
            if board[player_y][player_x] == '#' or board[player_y][player_x] == '|' or  board[player_y][player_x] == '~'  or  board[player_y][player_x] == '~' or board[player_y][player_x] == '_' or board[player_y][player_x] == ',':
                player_x -= 1
        
main()