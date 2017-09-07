import startscreen
import levels_board
import drawboard
import getch
import hero_create
import os
import thehangman
import sys
import end
import coldhot
import hall_of_fame
import time


def main():
    startscreen.print_start()
    level_one_board = drawboard.draw_board()
    board = drawboard.create_board(level_one_board)

    player_x = 5
    player_y = 2
    name = input("Enter your HappyHippie name: ")
    happiness_level, convincing_power = hero_create.hero_create()
    live = 20
    atc = 10
    score = 0
    exit_hangman = 0
    levels_board.printing_level_first_description()
    start = time.time()
    while True:
        print("\t Happines level = ", happiness_level, "\t", "\t", "\t", "\tchance to win = ",
              score, "\n\tPower of arguments = ", convincing_power, end='')
        place_before = board[player_y][player_x]
        board = drawboard.insert_player(board, player_x, player_y)
        drawboard.print_board(board)

        old_player_x = player_x
        old_player_y = player_y
        key = getch.getch()
        os.system("clear")

        if key == 'w':
            player_y -= 1
            if board[player_y][player_x] == '#' or board[player_y][player_x] == '|' or board[player_y][player_x] == '_' or board[player_y][player_x] == ',' or board[player_y][player_x] == '"':
                player_y += 1

        elif key == 'a':
            player_x -= 1
            if board[player_y][player_x] == '#' or board[player_y][player_x] == '|' or board[player_y][player_x] == '_' or board[player_y][player_x] == ',' or board[player_y][player_x] == '"':
                player_x += 1

        elif key == 's':
            player_y += 1
            if board[player_y][player_x] == '#' or board[player_y][player_x] == '|' or board[player_y][player_x] == '_' or board[player_y][player_x] == ',' or board[player_y][player_x] == '"':
                player_y -= 1

        elif key == 'd':
            player_x += 1
            if board[player_y][player_x] == '#' or board[player_y][player_x] == '|' or board[player_y][player_x] == '_' or board[player_y][player_x] == ',' or board[player_y][player_x] == '"':
                player_x -= 1

        elif key == 'q':
            hall_of_fame.write_to_file(name, score)
            sys.exit(0)

        if place_before == "$":
            print("You get a paycheck" + "\nYour level of happiness increased")
            happiness_level += 100
            place_before = " "

        if place_before == "O":
            print("Player happines level {} attack co-worker {}".format(happiness_level, convincing_power))
            happiness_level -= atc
            print("Co-worker sadness {} attack player {}".format(live, atc))
            live -= convincing_power
            if live <= 0:
                board[old_player_y][old_player_x] = '*'
                score += 1
                live = 20
            elif live > 0:
                board[old_player_y][old_player_x] = place_before

        if score > 0 and place_before == "B" and exit_hangman == 0:
            board[old_player_y][old_player_x] = ' '
            thehangman.game()
            level_second_board = drawboard.draw_second_board()
            board = drawboard.create_second_board(level_second_board)
            levels_board.printing_level_second_description()
            exit_hangman = 1

        if place_before == "~":
            print("")
            happiness_level -= 30

        if place_before == ">":
            coldhot.boss(score)
            game_time = int(time.time() - start)
            hall_of_fame.write_to_file(name, game_time)
            end.win_screen()

        if happiness_level <= 0:
            end.lose_screen()

        elif place_before != "O":
            board[old_player_y][old_player_x] = place_before


main()
