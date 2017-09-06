import startscreen
import end
import levels_board
import drawboard
import getch
import os
import hero_create
import stats
import time
import points
import hall_of_fame

def main():
    #startscreen.print_start()
    level_one_board = drawboard.draw_board()
    board = drawboard.create_board(level_one_board)

    player_x = 5
    player_y = 2
    
    hp, attack = hero_create.hero_create()
    #hp, attack = stats.hero_stats(hp, attack)
    live, atc = stats.enemy_stats(30, 15)
    score = 0
    name = input("Enter your name: ")
    start = points.start_game()
    while True:
        print("\tHero life = ", hp, "\t","\t","\t","\tscore = ", score, "\n\tHero attack = ", attack, end='')
        place_before = board[player_y][player_x]
        board = drawboard.insert_player(board, player_x, player_y)
        drawboard.print_board(board)

        old_player_x = player_x
        old_player_y = player_y
    
        key = getch.getch()
        os.system("clear")
        
        if key == 'w':
            player_y -= 1
            if board[player_y][player_x] == '#' or board[player_y][player_x] == '|' or  board[player_y][player_x] == '~' or board[player_y][player_x] == '_' or board[player_y][player_x] == ',':
                player_y += 1

        elif key == 'a':
            player_x -= 1
            if board[player_y][player_x] == '#' or board[player_y][player_x] == '|' or  board[player_y][player_x] == '~' or board[player_y][player_x] == '_' or board[player_y][player_x] == ',':
                player_x += 1

        elif key == 's':
            player_y += 1
            if board[player_y][player_x] == '#' or board[player_y][player_x] == '|' or  board[player_y][player_x] == '~' or board[player_y][player_x] == '_' or board[player_y][player_x] == ',':
                player_y -= 1
            
        elif key == 'd':
            player_x += 1
            if board[player_y][player_x] == '#' or board[player_y][player_x] == '|' or  board[player_y][player_x] == '~' or board[player_y][player_x] == '_' or board[player_y][player_x] == ',':
                player_x -= 1

        elif key == 'q':
            # points.end_game()
            end = points.end_game()
            hall_of_fame.write_to_file(name, start,  end, score)
            break
        
        elif place_before == "p":
            print("You find health potion")
            hp += 45
            place_before = " "
            
        elif place_before == "O":
            print("Player life {} attack enemy {}".format(hp, attack))
            hp -= atc
            print("Enemy life {} attack player {}".format(live, atc))
            live -= attack
            if live <= 0:
                board[old_player_y][old_player_x] = '*'
                points.score(score)
                score = points.score(score)
                live = 30
            elif live > 0:
                board[old_player_y][old_player_x] = place_before
        if hp <= 0:
            break

        elif place_before != "O":
            board[old_player_y][old_player_x] = place_before
main()