import startscreen
import end
import levels_board
import drawboard
import getch
import os
import hero_create
import stats

def main():
    #startscreen.print_start()
    level_one_board = drawboard.draw_board()
    board = drawboard.create_board(level_one_board)

    player_x = 5
    player_y = 2
    
    hp, attack = hero_create.hero_create()
    hp, attack = stats.hero_stats(hp, attack)
    live, atc = stats.enemy_stats(30, 15)

    while True:
        print("\tHero life = ", hp, "\n\tHero attack = ", attack)
        player_place = board[player_y][player_x]
        board = drawboard.insert_player(board, player_x, player_y)
        drawboard.print_board(board)
        key = getch.getch()
        os.system("clear")
        
        old_player_x = player_x
        old_player_y = player_y

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

        elif key == 'q':
            break

        if player_place == "O":
            print("Player life {} attack enemy {}".format(hp, attack))
            hp -= atc
            print("Enemy life {} attack player {}".format(live, atc))
            live -= attack
        #if live <= 0:
            #board[old_player_x[old_player_y]
        if hp <= 0:
            break
main()