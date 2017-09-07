import time
import os


def level_first_description():
    level_first_descryption = ('''
    ############################################################################################
    #The first board is your Hippie working space.                                             #
    #If he want to leave this place he has to talk to all his "0-look-like" co-workers.        #
    #Their arguments are not the best and they can decrease your level of happiness.           #
    #Just be patient, if you give them the time they will become bright stars in the company.  #
    #This experience will be quite helpful when you met your boss in next level.               #
    #                                                                                          #
    ############################################################################################ 
    ''')
    return level_first_descryption


def level_first_goals():
    level_first_goal = ('''
    ############################################################################################
    # First level goals:                                                                       #
    # - get the paycheck ($) to increase your level of happiness                               #
    # - talk to at least one of your co-worker (O) to increase chance to win with The Boss     #
    #    (You can go to the next level with at least one chance)                               #
    #                                                                                          #
    #  Be careful:                                                                             #
    #  - watch on your level of happiness                                                      #
    #  - don't touch the lake of tears ('~~~~')                                                #
    #                                                                                          #
    #                                                                                          #
    #Good luck!                                                                                #
    ############################################################################################
    ''')
    return level_first_goal


def level_one_board():

    level_one_board = '''
    ##############################################################
    #   B             |     ___,      ___,       |               #
    #                 |      O |       O |       |               #
    #                 |     ___,      ___,       |       $       #
    #                 |      O |       O |       |               #
    #                 |     ___,      ___,       |               #
    #______________            |       O |       |               #
    #                                                ____________#
    #    ~~~~ ~~    ~~~~       ___,    __,              ___,     #
    #                           O |      |       |       O |     #
    #              ~~~~~~      ___,    __,       |      ___,     #
    #                             |     O|       |         |     #
    #          ~~~             ___,    __,       |      ___,     #
    #___________     ~~~~       O |      |       |       O |     #
    #                |                        ~~~~~~~~~~   ______#
    #       $        |          ~~~~~~              ~~~~~~       #
    #                |___________ _________________    |         #
    #                            | $                   |         #
    ##############################################################
    '''
    return level_one_board


def level_second_description():
    level_second_descryption = ("""
    ##############################################################################
    # In this level, your Hippie will meet The Boss.                             #
    # Before you get to his office you have to walk through the salty            #
    # lake of tears those who were there before. Try not to touch them.          #
    #                                                                            #
    # When Hippie will finally meet The Boss, he will give you the final try.    #
    # If you are smart you will defeat him.                                      #
    # Yor new life is just right a corner! Stay cautious and good luck!          #
    #                                                                            #
    ##############################################################################
    """)
    return level_second_descryption


def level_second_board():

    level_second_board = '''
     ####################
     #                  #
      #~~         ~~    #
       #     ~~          #
        # ~~       ~~     #
         #           ~~    #
          ## ~~             ##
            #          ~~~~~~~################################################
            #                                                                #
            #~~~~~                                 _________________         #
            #          ~~~~~~~~~~~~~~~~~~~      __|@@@@@@@@@@@@@@@@@|__      #
            #                                  |@@@@@@@@@@@@@@@@@@@@@@@|__   #
            #                                __|@@@@@@@@@@@@@@@@@@@@@@@@@@|  #
            #~~~~~~~~~~~~~~~~               |@@@@@@@@@@  @@@@@@@@@@@@@@@@@|  #
            #                               |@@@@@@@@@    @@@@@@@@@@@@@@@@|  #
            #             ~~~~~~~~~~~~~~     """|@@@@@@  @@@@@@@@@@@@@@@@@|  #
            #                                    """"|@@@@@@@@@@@@@@@@@@@@|  #
            #                                         |@@@@@@@@@@@@@@@@@@@|  #
            #                ~~~~~~                 >>>> @@@@@@@@@@@@@@@@@|  #
            #                              ~~~~    ___|@@@@@@@@@@@@@@@@@@@|  #
            #                      ~~~~~~~~      _|@@@@@@@@@@@@@@@@@@@@@@@|  #
            #       ~~~~~~~~~~~~~~~~          __|@@@@@@@@@@@@@@@@@@@@@@@@@|  #
            #                                |@@@@@@@@@@@@@@@@@@@@@@@@@@@|   #
            #                                |@@@@@@@@@@@@@@@@@@@@@@@@@@|    #
            #                                 """|@@@@@@@@@@@@@@@@@@@@|"     #
            #                                     "|@@@@@@@@@@@@@@@@|"       #
            #                                       """"""""""""""""         #
            #                                                                #
            #                                                                #
            ##################################################################
    '''
    return level_second_board


def printing_level_first_description():
    print(level_first_description())
    time.sleep(5)
    print(level_first_goals())
    while True:
        ready = input("If you are ready click Y: ")
        if ready == "Y" or ready == "y":
            os.system('clear')
            break
    return


def printing_level_second_description():
    print(level_second_description())
    while True:
        ready = input("If you are ready click Y: ")
        if ready == 'Y' or ready == 'y':
            os.system('clear')
            break

    return
