import time
import os

start = (
"""
'||  ||`
 ||  ||
 ||''||   '''|.  '||''|, '||''|,  ||   //
 ||  ||  .|''||   ||  ||  ||  ||  ||  //
.||  ||. `|..||.  ||..|'  ||..|'   \,//
                  ||      ||        //
                 .||     .||       //
'||  ||`
 ||  ||   ''                   ''
 ||''||   ||  '||''|, '||''|,  ||  .|''|,
 ||  ||   ||   ||  ||  ||  ||  ||  ||..||
.||  ||. .||.  ||..|'  ||..|' .||. `|...
              .||     .||
     |         ||      ||
____/|\_____   ||
||||||||||||   ||                                     ______________
|||||  |||||   ||                                     |  _    _    |
||||||||||||___||_____________________________________| |_|  |_|   |
|||||  ||||| __||_____________________________________|  _    _    |
|||||||||||| |||||||||||______________________________| |_|  |_|   |
|||||||||||| ||||||  |||______________________________|  _    _    |
|||||  ||||| |||||||||||______________________________| |_|  |_|   |
|||||||||||| |||||||||||______________________________|  _    _    |
|||||||||||| ||||||  |||______________________________| |_|  |_|   |
|||||||||||| |||||||||||______________________________|    ___     |
|||||||||||| ||||||||||| _____________________________|   |   |    |
___________________________________________________________________________
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
===========================================================================
| | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
___________________________________________________________________________
""")

story = (
'''
###########################################################################
#                                                                         #
#                                                                         #
#This is a simple story about Happy Hippie. Well...he was happy years ago.#
#Now he ​misses​ his past ​life. He has to wear a truly uncomfortable suit   #
#and shiny shoes. You know ​that ​this is not the way of ​life ​that works ​for#
#him so help him to get out of there before he loses all the joy of life. #
#If that happens, he will become a low paid corpo-worker forever.         #
#                                                                         #
#                                                                         #
###########################################################################
''')

autors = (
'''
###########################################################################
#                                                                         #
#                          Happy Hippie                                   #
#                                                                         #
#                    The game was created by:                             #
#                   Magdalena Kiełkowicz-Werner                           #
#                               &                                         #
#                         Adam Łupikasza                                  #
#                                                                         #
#                                                                         #
###########################################################################
''')

instructions = (
'''
##########################################################################
# If you want to move your Hippie just press one of the WASD buttons:    #
#            W - to move up                                              #
#            S - to move down                                            #
#            A - to move left                                            #
#            D - to move right                                           #
# When you meet your smart and bad boss just play Hot-Worm game with him.#
# If you win he will be defeted and you will get out.                    #
##########################################################################
''')

def print_start():
    for letter in start:
        print(letter, end='')
        time.sleep(0.004)
    time.sleep(2)
    os.system("clear")
    print(autors)
    time.sleep(4)
    os.system("clear")
    print(story)
    time.sleep(4)
    os.system("clear")
    print(instructions)
    time.sleep(4)
    os.system("clear")
a
