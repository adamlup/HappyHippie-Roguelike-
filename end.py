import time
import sys

win = (
    '''
###########################################################################
#                                                                         #
#                                                                         #
#                                                                         #
#                             YOU WIN                                     #
#                                                                         #
#                                                                         #
#                                                                         #
#                                                                         #
#                                                                         #
###########################################################################
'''
)

lose = (
    '''
###########################################################################
#                                                                         #
#                                                                         #
#                                                                         #
#                             YOU LOSE                                    #
#                                                                         #
#                                                                         #
#                                                                         #
#                                                                         #
#                                                                         #
###########################################################################
'''
)


def win_screen():
    print(win)
    time.sleep(2)
    sys.exit(0)


def lose_screen():
    print(lose)
    time.sleep(2)
    sys.exit(0)
